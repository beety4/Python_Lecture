
def getResult():
    #result = [3, 6, 9]
    result = {'1': 'hi', '2': 'nice'}
    return result

from django import forms
class MyForm(forms.Form):
    value = forms.CharField(label='Input Data')

