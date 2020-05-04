from django.forms import SelectDateWidget, Select, FileInput


class DropzoneFileInput(FileInput):
    template_name = 'widgets/dropzone_file.html'
