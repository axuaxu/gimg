from django.contrib import admin
from django.core import serializers
from get_img.models import ImageStore,ImageStage,ImageSelected,Amazon
import shutil,sys
from pathlib import Path
# Register your models here.


def save_to_stage(modeladmin, request, queryset):
    for object in queryset:
        Sorder = object.ImageOrder
        Surl = object.ImageURL
        Sref = object.ImageREF
        Stitle = object.ImageTitle
        Skeyword = object.ImageKeyword
        imS = ImageStage(ImageOrder=Sorder,ImageURL=Surl,ImageREF=Sref,ImageTitle=Stitle,ImageKeyword=Skeyword)
        imS.save()
    save_to_stage.short_description = "Save To Stage"

def save_to_selected(modeladmin, request, queryset):
    for object in queryset:
        Sorder = object.ImageOrder
        Surl = object.ImageURL
        Sref = object.ImageREF
        Stitle = object.ImageTitle
        Skeyword = object.ImageKeyword
        imS = ImageSelected(ImageOrder=Sorder,ImageURL=Surl,ImageREF=Sref,ImageTitle=Stitle,ImageKeyword=Skeyword)
        imS.save()
    save_to_selected.short_description = "Save To Selected"

def export_to_xml(modeladmin, request, queryset):
    i = 0
    for object in queryset:
        i = i + 1
        xmlName = object.ImageKeyword
    #xml_serializer = XMLSerializer()
    #Xdata = serializers.serialize("xml", ImageSelected.objects.all())
    xmlName="./get_img/xmltmp/"+str(i)+"-"+xmlName.replace(' ','-')+"s.xml"
    with open(xmlName, "w") as out:
         serializers.serialize("xml",ImageSelected.objects.all(),stream=out)

    export_to_xml.short_description = "Export To XML"

class ImageStoreAdmin(admin.ModelAdmin):

    # ...
    list_display = ('id','ImageOrder','image_tag','ImageTitle','ImageREF','ImageKeyword')
    #list_editable = ('ImageOrder','ImageTitle')
    list_filter = ['ImageKeyword']
    ordering = ['id']
    search_fields = ['ImageTitle']
    #actions = [save_to_stage]
    actions = [save_to_selected]

class ImageStageAdmin(admin.ModelAdmin):

    # ...
    list_display = ('id','ImageOrder','image_tag','ImageTitle','ImageREF','ImageKeyword')
    #list_editable = ('ImageOrder','ImageTitle')
    list_filter = ['ImageKeyword']
    ordering = ['id']
    search_fields = ['ImageTitle']
    #actions = [save_to_selected]

    def duplicate_event(modeladmin, request, queryset):
        for object in queryset:
            object.id = None
            object.save()
        duplicate_event.short_description = "Duplicate selected record"

class ImageSelectedAdmin(admin.ModelAdmin):

    # ...
    list_display = ('id','ImageOrder','image_tag','ImageTitle','ImageREF','ImageKeyword')
    list_editable = ('ImageOrder','ImageTitle')
    list_filter = ['ImageKeyword']
    ordering = ['ImageREF']
    search_fields = ['ImageTitle']
    actions = [export_to_xml,save_to_stage]

class AmazonAdmin(admin.ModelAdmin):
    list_display = ('id','asin','desc')

admin.site.register(ImageStore,ImageStoreAdmin)
admin.site.register(ImageStage,ImageStageAdmin)
admin.site.register(ImageSelected,ImageSelectedAdmin)

admin.site.register(Amazon,AmazonAdmin)