import requests

KINDS = {'animal':0, 'vegetable':1, 'mineral':2, 'concept':3, 'unknown':4}
url_prefix = 'http://dota.happylyang.com:8050/execute?wait=2&'

print 'Initializing...plz wait...'

# first choose kinds
script_first = 'function+main%28splash%29%0D%0A++local+url+%3D+splash.args.url%0D%0A++assert%28splash%3Ago%28%27http%3A%2F%2Fy.20q.net%2Fgsq-en%27%29%29%0D%0A++assert%28splash%3Await%282%29%29%0D%0A++splash%3Aevaljs%28%22var+doc+%3D+document.getElementsByName%28%27mainFrame%27%29%5B0%5D.contentDocument%3Bdoc.getElementsByName%28%27age%27%29%5B0%5D.value%3D123%3Bdoc.getElementsByName%28%27submit%27%29%5B0%5D.click%28%29%3B%22%29%0D%0A++assert%28splash%3Await%282%29%29%0D%0A++local+hrefs+%3D+splash%3Aevaljs%28%22var+doc+%3D+document.getElementsByName%28%27mainFrame%27%29%5B0%5D.contentDocument%3Bvar+href%3D+doc.getElementsByTagName%28%27b%27%29%5B1%5D.getElementsByTagName%28%27a%27%29%3Bvar+arr%3Dnew+Array%28%29%3Bfor%28var+h%3D0%3Bh%3Chref.length%3Bh%2B%2B%29%7Barr.push%28href%5Bh%5D.href%29%7D%3Barr%22%29%0D%0A%0D%0A++return+%7B%0D%0A++++hrefs%3Dhrefs%2C%0D%0A++%7D%0D%0Aend'
res = requests.get("{0}lua_source={1}".format(url_prefix,script_first)).json()

if not 'hrefs' in res or len(res['hrefs'])!= 5:
    print 'Network Error,plz try again...'
else:
    print 'Input a kind name(animal, vegetable, mineral, concept, unknown):'
    kind = raw_input()
    quiz_url = res['hrefs'][KINDS[kind]]
    print 'Getting questions...'
    i = 0
    while True:
        script = 'function+main%28splash%29%0D%0A++assert%28splash%3Ago%28splash.args.url%29%29%0D%0A++assert%28splash%3Await%282%29%29%0D%0A++local+hrefs+%3D+splash%3Aevaljs%28%22var+doc+%3D+document.getElementsByName%28%27mainFrame%27%29%5B0%5D.contentDocument%3Bvar+b%3Ddoc.getElementsByTagName%28%27b%27%29%5B0%5D%3Bvar+href%3Db.getElementsByTagName%28%27a%27%29%3Bvar+arr%3Dnew+Array%28%29%3Bfor%28var+h%3D0%3Bh%3Chref.length%3Bh%2B%2B%29%7Barr.push%28href%5Bh%5D.href%29%7D%3Barr%22%29%0D%0A++local+text+%3D+splash%3Aevaljs%28%22var+doc+%3D+document.getElementsByName%28%27mainFrame%27%29%5B0%5D.contentDocument%3Bvar+b%3Ddoc.getElementsByTagName%28%27b%27%29%5B0%5D%3Bb.childNodes%5B0%5D.textContent%22%29%0D%0A++return+%7B%0D%0A++++hrefs%3Dhrefs%2C%0D%0A++++text%3Dtext%0D%0A++%7D%0D%0Aend'
        res = requests.get("{0}lua_source={1}&url={2}".format(url_prefix,script, quiz_url)).json()
        print u"{0} yes or no?".format(res['text'])
        ans = raw_input()
        ans = 0 if ans == 'yes' or ans == 'Yes' else 1
        quiz_url = res['hrefs'][ans]
        i += 1
        if i == 20 :
            print 'You win'
            break
        if not res['hrefs']:
            break
    
