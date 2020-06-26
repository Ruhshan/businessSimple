from django.db import models

# Create your models here.
class BaseModel(models.Model):
    """
    Base of all models with bare minimum fields. Abstract.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey("auth.User", related_name="+", blank=True, null=True)
    updated_by = models.ForeignKey("auth.User", related_name="+", blank=True, null=True)
    version = models.IntegerField(default=0)
    is_locked = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True


class CodedBase(BaseModel):
    """
    BaseModel with the `power of code`. The `generate_code` method holds the logic for
    generating the code which can easily be overriden.

    If `generate_code` is overriden and the generated code does not comply with the
    `__str__` method given, then `__str__` must also be overriden if not already done.
    """
    _prefix = 'C'
    code = models.CharField(unique=True, max_length=255)


    class Meta:
        abstract = True

    def __str__(self):
        # Use Python3.6 formatting? TODO
        if hasattr(self, "short_code"):
            return "{}-{}".format(getattr(self, 'short_code'), getattr(self, 'title'))
        elif hasattr(self, "name"):
            return "{} - {}".format(self.code, getattr(self, 'name'))
        elif hasattr(self, "title"):
            return "{}".format(getattr(self, 'title'))


        return "{}".format(self.code)


    def generate_code(self):
        """
        Takes up the prefix, joins `n+1`-th number where `n` is the highest code integer, with `-`
        """
        model_type = type(self)
        if model_type.objects.exists():
            # select last generated code number
            last_digit = int(model_type.objects.all().order_by("-pk")[0].code.split("-")[1])
        else:
            last_digit = 1

        return "{}-{}".format(self._prefix, last_digit+1)

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = self.generate_code()

        return super(CodedBase, self).save(*args, **kwargs)