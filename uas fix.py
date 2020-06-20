import urllib, json

url = "https://coronavirus-19-api.herokuapp.com/countries/indonesia"
respon = urllib.urlopen(url)
data = json.loads(respon.read())
print "Jumlah pasien positif covid19 \t: %s" % data['cases'],"\nPasien yang sembuh \t: %s" % data['recovered'],"\nPasien yang meninggal dunia \t: %s" % data['deaths']