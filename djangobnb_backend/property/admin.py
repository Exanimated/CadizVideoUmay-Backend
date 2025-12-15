from django.contrib import admin

from .models import Property, Reservation


class ReservationInline(admin.TabularInline):
	model = Reservation
	extra = 0
	readonly_fields = (
		"start_date",
		"end_date",
		"number_of_nights",
		"guests",
		"total_price",
		"created_by",
		"created_at",
	)
	can_delete = True


class PropertyAdmin(admin.ModelAdmin):
	list_display = ("tittle", "landlord", "price_per_night", "created_at")
	inlines = [ReservationInline]


admin.site.register(Property, PropertyAdmin)
admin.site.register(Reservation)
