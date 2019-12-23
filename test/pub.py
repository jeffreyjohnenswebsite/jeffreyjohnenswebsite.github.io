import bibtexparser

def format_authors(entry):
  return " and ".join([" ".join([author.split()[0][0].upper(), author.split()[1]]) for author in entry["author"].split(" and ")])

def format_volume(entry):
  x = entry.get("volume", "")
  return "Vol. " + x + ". " if len(x) else ""

def format_year_pages(entry):
  year = entry.get("year", "")
  pages = entry.get("pages", "")
  if len(year) and len(pages):
    return "%s, %s. " % (year, pages)
  elif len(year):
    return "%s. " % (year,)
  return "%s." % (pages,)

def format_download(entry):
  link = entry.get("link", "")
  if len(link):
    return '<a href="%s", target="_blank", class="material-icons", style="text-decoration:none;font-size:1.2vmax">get_app</a>' % (link,)
  return ""

def entry_to_text(entry):
  return '%s. "%s". In %s. %s%s%s' % (
    format_authors(entry), 
    entry["title"], 
    entry["booktitle"], 
    format_volume(entry),
    format_year_pages(entry),
    entry.get("addendum",""))

def entry_to_html(entry):
  return '%s %s. "%s". In <i>%s</i>. %s%s%s' % (
    format_download(entry),
    format_authors(entry), 
    entry["title"], 
    entry["booktitle"], 
    format_volume(entry),
    format_year_pages(entry),
    entry.get("addendum",""))

if __name__ == "__main__":

  path = "/Users/Jeff/SFU/PhD/CV/pub.bib"
  with open(path) as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)
  
  for entry in bib_database.entries:
    print(entry_to_html(entry) + "<br><br>")