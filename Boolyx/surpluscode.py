## From Views.py

def BookReader(request, pk):
    
    base = settings.MEDIA_ROOT
    name = Book.objects.get(pk=pk)
    print("File: ", name)
    name = str(name)
    name = str(name.replace(" ", "_"))
    path = "{0}\{1}.txt".format(base, name)
    with open(path, "r", encoding="utf-8-sig") as f:
        reading = f.read()#[line.rstrip() for line in f]
        bookreads = {"file" : reading}
        return render(request, 'bookreader.html', bookreads, content_type = "text")


def BookReader(request):
    with open('/path / to /name.pdf', 'rb') as pdf:
        response = HttpResponse(pdf.read(),content_type='application/pdf')
        response['Content-Disposition'] = 'filename=some_file.pdf'
        return response


class BookList(ListView):
    model = Book
    template_name = 'book/book_list.html'
    context_object_name = 'book'
    queryset = Book.objects.prefetch_related('authors')
    paginate_by = 10
    def get_context_data(self, **kwargs):
        context = super(BookList,self).get_context_data(**kwargs)
        book_list =Book.objects.all()
        paginator = Paginator(book_list,self.paginate_by)

        page = self.request.GET.get('page')
        try:
            book_list = paginator.page(page)
        except PageNotAnInteger:
            file_book = paginator.page(1)
        except EmptyPage:
            book_list = paginator.page(paginator.num_pages)

        context['book_list'] = book_list
        return context