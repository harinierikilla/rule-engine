from django.urls import path
from .views import RuleEngine, RuleFormView

urlpatterns = [
    path('',RuleFormView.as_view(), name='rule_form'),
    path('create_rule/', RuleEngine.as_view(), name='create_rule'),
    # path('combine_rules/', CombineRuleView.as_view(), name='combine_rules'),  
    # path('evaluate_rule/', EvaluateRuleView.as_view(), name='evaluate_rule'),  
    
]
