from estate_habi.views import get_estate_view

__author__ = 'kcastanedat'

PATH_AND_METHODS = {
    '/dev/estate/?p': ['GET', get_estate_view]
}
