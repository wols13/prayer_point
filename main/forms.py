from django import forms

class AddPPForm(forms.Form):
    add_pp_full_name = forms.CharField(label='Your name', max_length=32)
    add_pp_email = forms.EmailField(label='Email', max_length=64)
    add_pp_bible_ref = forms.CharField(label='Bible ref', max_length=64, widget=forms.TextInput(
                                       attrs={'placeholder': 'Examples: Psalm 23:1; John 1:3-5 & 19-21',
                                              'onkeyup': 'updateBibleRefCount()'}))
    add_pp_content = forms.CharField(label='Prayer point', max_length=512, widget=forms.Textarea(
                                     attrs={'onkeyup': 'updateContentCount()'}))
    add_pp_cat_cons = forms.BooleanField(required=False)
    add_pp_cat_fami = forms.BooleanField(required=False)
    add_pp_cat_nati = forms.BooleanField(required=False)
    add_pp_cat_warf = forms.BooleanField(required=False)
    add_pp_cat_dire = forms.BooleanField(required=False)
    add_pp_cat_favo = forms.BooleanField(required=False)
    add_pp_cat_prot = forms.BooleanField(required=False)
    add_pp_cat_weal = forms.BooleanField(required=False)
    add_pp_cat_enco = forms.BooleanField(required=False)
    add_pp_cat_heal = forms.BooleanField(required=False)
    add_pp_cat_prov = forms.BooleanField(required=False)
    add_pp_cat_wors = forms.BooleanField(required=False)