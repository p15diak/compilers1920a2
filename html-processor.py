import re

#Συνάρτηση μετατροπής html entities

def htmlEntities(m):
  if(m.group(0)=='&amp;'):
    return '&'
  elif (m.group(0)=='&gt;'):
    return '>'
  elif (m.group(0)=='&lt;'):
    return '<'
  elif (m.group(0)=='&nbsp;'):
    return ' '

#Απαντήσεις στα ερωτήματα-Κανονικές εκφράσεις

rexp1 = re.compile(r'<title>(.+?)</title>') #.1 (Matching tou <title> μέσα στο κείμενο )

rexp2 = re.compile(r'<!--.*?-->',re.DOTALL) #.2 (Matching των comments σε όλο το κείμενο )

rexp3 = re.compile(r'<(script|style).*?>.*?</(script|style)>',re.DOTALL) #3.Matching  των  script/style στο κείμενο

rexp4 = re.compile(r'<a.+?href="(.*?)".*?>(.*?)</a>',re.DOTALL) #.4 Matching των  link

rexp51 = re.compile(r'<.+?>|</.+?>',re.DOTALL) #5.1 Εξαγωγή διπλών tags (<> </>) Μatching των διπλών tags στο κείμενο (<> </>)
rexp52 = re.compile(r'<.+?/>',re.DOTALL) #5.2 Εξαγωγή self closing  tags  (</>) Μatching self closing tags στο κείμενο (</>)

rexp6 = re.compile(r'&(amp|gt|lt|nbsp);') #.6 Μatching των html entities στο κείμενο

rexp7 = re.compile(r'\s+') #.7  Matching whitespace χαρακτήρων μέσα στο κείμενο



with open('testpage.txt','r') as fp: #Ανοιγμα txt με read perimision
  text = fp.read()
  m = rexp1.search(text)
  print(m.group(1)) #.Εξαγωγή τίτλου και εκτύπωση
  text = rexp2.sub(' ',text) #Απαλοιφή σχολίων

  text = rexp3.sub(' ',text) #απαλοιφή script style

  for m in rexp4.finditer(text):
    print('{} {}'.format(m.group(1),m.group(2)))#εμφανίζουμε τα links

  text = rexp51.sub(' ',text)#Απαλοιφή ολων των διπλών tags
  text = rexp52.sub(' ',text) #Απαλοιφή ολων των  self closing tags

  text = rexp6.sub(htmlEntities,text) #Μετατροπη Html entities

  text = rexp7.sub(' ',text) #Μετατροπή whitespaces σε ενα κενό

  print(text)#Τελικό κείμενο
