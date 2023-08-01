
# Option 1: Admin view has any table (models ) in a separate view, even if then has relationship

# from django.contrib import admin

# from .models import Question, Choice

# admin.site.register([Question, Choice])


# Option 2: Admin view has just few tables (models ) and leverage the views with the relationships (nested views)

from django.contrib import admin

from .models import Choice, Question


class ChoiceInline(admin.TabularInline):  # you also has StakeInLine view (tree view): admin.StackedInline
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]


admin.site.register(Question, QuestionAdmin)