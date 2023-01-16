from typing import List

from django.db.models import Model


class BarChart(object):
    """"""
    chart_type = 'bar'
    
    def __init__(self,
                 data: List[List[dict]],
                 expressions: List[str],
                 label: List[str],
                 model: Model,
                 x_field: str,
                 y_field: str,
                 background_color: List[str] = None):
        self.__validate(expressions=expressions, label=label, model=model, x_field=x_field, y_field=y_field, background_color=background_color)
        self.data = data
        self.expressions = expressions
        self.label = label or ['']
        self.model = model
        self.x_field = x_field
        self.y_field = y_field
        self.background_color = background_color or ['rgb(120, 174, 200)']
        
    def __validate(self, expressions, label, model, x_field, y_field, background_color):
        if not isinstance(expressions, list) and not isinstance(expressions, tuple):
            raise ValueError('Expressions argument is not list or tuple')
        if not isinstance(label, list) and not isinstance(label, tuple):
            raise ValueError('Label argument is not list or tuple')
        if background_color and not isinstance(background_color, list) and not isinstance(background_color, tuple):
            raise ValueError('background_color argument is not list or tuple')
        
        model_attrs = [x.name for x in model._meta.get_fields()]
        
        if x_field not in model_attrs:
            raise ValueError(f'Model {model} has no attribute "{x_field}"')
        if y_field not in model_attrs:
            raise ValueError(f'Model {model} has no attribute "{y_field}"')
        
    def generate_context(self):
        context_data = {
            'chart_type': self.chart_type,
            'datasets': []
        }
            
        context_data = {
            'chart_type': self.chart_type,
            'datasets': []
        }
        for i in range(0, len(self.data)):
            data_to_add = {}
            data_to_add['data'] = self.data[i]
            try:
                data_to_add['label'] = self.label[i]
            except:
                data_to_add['label'] = self.label[0]
            try:
                data_to_add['backgroundColor'] = self.background_color[i]
            except:
                data_to_add['backgroundColor'] = self.background_color[0]
            context_data['datasets'].append(data_to_add)
            
        return dict(context_data)