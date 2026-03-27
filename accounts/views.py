from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Profile


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    template_name = "accounts/account_update.html"
    fields = ['display_name']
    
    def get_object(self):
        return Profile.objects.get(user__username=self.kwargs['username'])
    
    def get_success_url(self):
        return reverse_lazy('accounts:update', kwargs={'username': self.object.user.username})