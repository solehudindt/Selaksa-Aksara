from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, View
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.utils import timezone
from .forms import CheckoutForm, FormBuktiBayar
from .models import Barang, BarangOrder, Order, BillingAddress, BuktiBayar

# Create your views here.


@user_passes_test(lambda u: u.is_superuser)
def adminOrderView(request):
    context = {
        'order': Order
    }
    return render(request, 'admin-view.html', context)


# def list_brg(request):
#     context = {
#         'barangs': Barang.objects.all()
#     }
#     return render(self.request, 'product-page.html', context)


class IndexView(ListView):
    model = Barang
    template_name = "shop.html"
    paginate_by = 10

    # def get_context(self, *args, **kwargs):
    #     context = super().get_context(*args, **kwargs)
    #     shop = "shop"
    #     context["nbar"]: shop
    #     return context


class OrderSumView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, dipesan=False)
            context = {
                'object': order
            }
            return render(self.request, 'order_sum.html', context)
        except ObjectDoesNotExist:
            messages.error(self.request, "Anda belum memiliki pesanan")
            return redirect("/")


class BarangDetailView(DetailView):
    model = Barang
    template_name = "product-page.html"


@login_required
def add_to_cart(request, slug):
    brg = get_object_or_404(Barang, slug=slug)
    brg_order, created = BarangOrder.objects.get_or_create(
        barang=brg,
        user=request.user,
        dipesan=False
    )
    qs_order = Order.objects.filter(user=request.user, dipesan=False)
    if qs_order.exists():
        order = qs_order[0]
        if order.barangs.filter(barang__slug=brg.slug).exists():
            brg_order.jumlah += 1
            brg_order.save()
            messages.info(request, "Jumlah barang ditambahkan")
        else:
            order.barangs.add(brg_order)
            messages.info(request, "Barang dimasukan kedalam Keranjang")
    else:
        tgl_pesan = timezone.now()
        order = Order.objects.create(user=request.user, tgl_pesan=tgl_pesan)
        order.barangs.add(brg_order)
        messages.info(request, "Barang dimasukan kedalam Keranjang")
    return redirect("core:order-sum")


@login_required
def remove_from_cart(request, slug):
    brg = get_object_or_404(Barang, slug=slug)
    qs_order = Order.objects.filter(user=request.user, dipesan=False)
    if qs_order.exists():
        order = qs_order[0]
        if order.barangs.filter(barang__slug=brg.slug).exists():
            brg_order = BarangOrder.objects.filter(
                barang=brg,
                user=request.user,
                dipesan=False,
            )[0]
            order.barangs.remove(brg_order)
            brg_order.delete()
            messages.info(request, "Barang dihapus dari Keranjang")
            return redirect("core:produk", slug=slug)
        else:
            messages.info(request, "Barang tidak dalam Keranjang")
            return redirect("core:produk", slug=slug)
    else:
        messages.info(request, "Anda belum membuat pesanan")
        return redirect("core:produk", slug=slug)


@login_required
def remove_single(request, slug):
    brg = get_object_or_404(Barang, slug=slug)
    qs_order = Order.objects.filter(user=request.user, dipesan=False)
    if qs_order.exists():
        order = qs_order[0]
        if order.barangs.filter(barang__slug=brg.slug).exists():
            brg_order = BarangOrder.objects.filter(
                barang=brg,
                user=request.user,
                dipesan=False,
            )[0]
            brg_order.jumlah -= 1
            brg_order.save()
            messages.info(request, "Jumlah barang dikurangi")
            return redirect("core:order-sum")
        else:
            messages.info(request, "Barang tidak dalam Keranjang")
            return redirect("core:produk", slug=slug)
    else:
        messages.info(request, "Anda belum membuat pesanan")
        return redirect("core:produk", slug=slug)


class CheckoutView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        form = CheckoutForm()
        context = {
            'form': form
        }

        return render(self.request, 'checkout-page.html', context)

    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST or None)
        try:
            order = Order.objects.get(user=self.request.user, dipesan=False)
            if form.is_valid():
                print("form is valid")
                alamat = form.cleaned_data.get('alamat')
                ket_lain = form.cleaned_data.get('ket_lain')
                provinsi = form.cleaned_data.get('provinsi')
                kode_pos = form.cleaned_data.get('kode_pos')
                save_info = form.cleaned_data.get('save_info')
                billing_address = BillingAddress(
                    user=self.request.user,
                    alamat=alamat,
                    ket_lain=ket_lain,
                    provinsi=provinsi,
                    kode_pos=kode_pos
                )
                billing_address.save()
                order.dipesan = True
                order.billing_address = billing_address
                messages.success(
                    self.request, 'Pesanan sudah dicatat akan diproses setelah anda melakukan pembayaran invoice anda : ' + order.invoice)
                order.save()
                return redirect('core:inputBukti')
            messages.warning(self.request, "Failed")
            return redirect("core:checkout")
        except ObjectDoesNotExist:
            messages.error(self.request, "Anda belum memiliki pesanan")
            return redirect("/")


@login_required
def inputBukti(request):
    if request.method == 'POST':
        form = FormBuktiBayar(request.POST, request.FILES)

        if form.is_valid():
            invoice = form.cleaned_data.get('invoices')
            foto = form.cleaned_data.get('foto')
            obj = BuktiBayar.objects.create(
                invoice=invoice,
                foto=foto
            )
            print("wkwkwk")
            obj.save()
            return redirect('/')
        else:
            # print("wkwkwk3")
            # messages.error(request, "salah")
            return redirect('/')

    else:
        form = FormBuktiBayar()

    return render(request, 'form-bukti.html', {'form': form})
