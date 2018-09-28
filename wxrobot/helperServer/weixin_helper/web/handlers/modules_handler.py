# -*- coding: utf-8 -*- 
__author__ = 'jasonzhang'

import math
# import urlparse
import urllib.parse as urlparse
import urllib
import tornado.web

PAGINATOR_DISPLAY_COUNT = 7  # 分页默认显示页数（注：多于此数仅显示此页数）

class Paginator(tornado.web.UIModule):
    """Pagination links display."""

    def render(self, page_index, page_size, total_count):
        page_count = int(math.ceil(float(total_count) / page_size)) if total_count else 0

        def update_querystring(url, **kwargs):
            base_url = urlparse.urlsplit(url)
            query_args = urlparse.parse_qs(base_url.query)
            query_args.update(kwargs)
            for arg_name, arg_value in kwargs.items():
                if arg_value is None:
                    if query_args.has_key(arg_name):
                        del query_args[arg_name]

            query_string = urlparse.urlencode(query_args, True)
            return urlparse.urlunsplit((base_url.scheme, base_url.netloc,
                                        base_url.path, query_string, base_url.fragment))

        def get_page_url(page_index):
            # don't allow ?page=1
            if page_index < 1:
                page_index = None
            return update_querystring(self.request.uri, page_index=page_index)

        next = page_index + 1 if page_index < page_count else None
        previous = page_index - 1 if page_index > 1 else None

        start_index = 1
        end_index = page_count + 1
        if page_count > PAGINATOR_DISPLAY_COUNT:
            half = int(math.ceil(PAGINATOR_DISPLAY_COUNT/2))
            start_index = min(max(page_index - half, 1), page_count - PAGINATOR_DISPLAY_COUNT + 1)
            end_index = start_index + PAGINATOR_DISPLAY_COUNT

        return self.render_string('modules/pagination.html', page_index=page_index, page_count=page_count, next=next,
                                  previous=previous, get_page_url=get_page_url,
                                  display_range=range(start_index, end_index))