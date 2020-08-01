from django.forms import Select

class VueSelect(Select):
    def __init__(self, attrs=None, choices=()):
        super().__init__(attrs, choices)

    def render(self, name, value, attrs=None, renderer=None):
        attrs["v-model"]="price"
        context = self.get_context(name, value, attrs)
        rendered = self._render(self.template_name, context, renderer)
        options = """
            <option>-------</option>
            {% verbatim %}
            <option v-for="price in prices" value="{{ price.id }}">{{ price.buying }}</option>
            {% endverbatim %}
            </select>
        """
        rendered_with_options = rendered.replace("</select>",options)
        return rendered_with_options

