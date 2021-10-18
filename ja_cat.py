#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv
from mechanicalsoup import StatefulBrowser

ja_cat_url = "https://ja.cat"
input_name ="link-url"
form_class = ".formulario"
browser = StatefulBrowser(user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36")
browser.open(ja_cat_url)

browser.select_form(form_class)
browser[input_name] = argv[1] 
browser.submit_selected()

shortend_url =  browser.page.select(".result-box")[0]["value"]

print (shortend_url)

