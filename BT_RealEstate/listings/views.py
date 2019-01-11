from django.shortcuts import get_object_or_404, render
from .models import Listing
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.

# Listings
def index(request):
  ## Fetch Listing ##
  listings = Listing.objects.order_by('-list_date').filter(is_published=True)

  ## Pagination
  paginator = Paginator(listings, 6)
  page = request.GET.get('page')
  page_listings = paginator.get_page(page)

  ## List ##
  context = {
    'listings': page_listings
  }
  return render(request, 'listings/listings.html', context)

# Listing
def listing(request, listing_id):
  listing = get_object_or_404(Listing, pk=listing_id)

  context = {
    'listing': listing,
  }

  return render(request, 'listings/listing.html', context)

# Search
def search(request):
  return render(request, 'listings/search.html')