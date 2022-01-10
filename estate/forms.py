class BusinessForms(forms.ModelForm):
    email=forms.EmailField()
    class Meta:
        model=Business
        fields= ['name','email','business_image','location']
