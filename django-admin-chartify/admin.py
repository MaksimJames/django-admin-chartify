import json

from django.contrib.admin import ModelAdmin


class ChartifyModelAdmin(ModelAdmin):
    chart = None
    
    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(request, extra_context=extra_context)
        self.chart.queryset = response.context_data['cl'].queryset
        response.context_data['chart'] = json.dumps(self.chart.generate_context())

        return response