from django.forms import Select


class VueSelect(Select):
    def __init__(self, attrs=None, choices=()):

        super().__init__(attrs, choices)

    def render(self, name, value, attrs=None, renderer=None):
        attrs["v-model"] = "price"
        context = self.get_context(name, value, attrs)
        rendered = self._render("operation/empty_option.html", context, renderer)
        return rendered

