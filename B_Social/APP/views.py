from django.shortcuts import render, redirect

def index(request):
    return render(request,'base.html')


def login_view(request):
    # Kullanıcı giriş işlemi başarıyla gerçekleştiği kontrolü
    if user_logged_in_successfully:
        return redirect('home')  # Yönlendirilecek URL'yi belirtin
    else:
        # Giriş başarısız ise, hata mesajı ile birlikte giriş sayfasını tekrar göster
        return render(request, 'login.html', {'error_message': 'Invalid credentials'})