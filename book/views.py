from django.shortcuts import render, get_object_or_404
from .models import Book
from django.shortcuts import render, redirect
from .forms import BookForm
from .models import Book
import fitz  
from django.shortcuts import render, get_object_or_404
from .models import Book
import fitz

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    
    return render(request, 'book_detail.html', {'book': book})
from django.shortcuts import render, get_object_or_404
from .models import Book
import fitz

def pdf_view(request, book_id):
    # Get the book object
    book = get_object_or_404(Book, pk=book_id)

    # Get the path to the PDF file
    pdf_path = book.pdf.path  # Update this line to use the correct attribute for the PDF field

    # Open the PDF document using PyMuPDF
    pdf_document = fitz.open(pdf_path)

    # Lists to store text, image, and table elements from the PDF
    text_elements = []
    image_elements = []
    table_elements = []

    # Iterate through each page of the PDF document
    for page_number in range(pdf_document.page_count):
        # Get the current page
        page = pdf_document[page_number]

        # Extract text from the page and append to the text elements list
        text_elements.append(page.get_text())

        # Extract images from the page and append base64-encoded images to the image elements list
        images = page.get_images(full=True)
        for img_index, img_info in enumerate(images):
            base64_image = img_info[1]
            image_elements.append(f"data:image/png;base64,{base64_image}")

        # Check if the get_tables method is available on the page object
        if hasattr(page, 'get_tables'):
            # Extract tables from the page and append table data to the table elements list
            tables = page.get_tables()
            for table_index, table in enumerate(tables):
                table_data = []
                for row_index, row in enumerate(table):
                    row_data = [col.get_text() for col in row]
                    table_data.append(row_data)
                table_elements.append(table_data)

    # Close the PDF document
    pdf_document.close()

    # Render the PDF view template with the extracted elements
    return render(request, 'pdf_view.html', {
        'book': book,
        'text_elements': text_elements,
        'image_elements': image_elements,
        'table_elements': table_elements,
    })
