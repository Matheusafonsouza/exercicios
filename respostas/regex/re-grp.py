import re
import datetime

entry = """
Voluptatibus maxime iure eos explicabo aspernatur. Commodi consectetur fugit neque facere. Aspernatur consectetur inventore ipsa harum reprehenderit. Fugit distinctio perferendis eaque. Pariatur nostrum hic dicta at delectus. Nesciunt delectus repellendus doloremque. Illo veritatis vitae odit consequuntur. Nostrum doloribus molestiae nihil laudantium ad. Architecto aliquid aspernatur aspernatur. Cum officiis veritatis nam velit tempora nulla. Aspernatur molestias sit. Est ratione voluptates illo eligendi similique.

Optio sint iste provident praesentium ratione ex. Mollitia incidunt minus 1520-08-05. Aperiam hic et libero esse. Aliquid omnis alias recusandae. Ut eaque adipisci ad esse mollitia. Minus adipisci iusto aliquam numquam.

Aut enim sed praesentium saepe cum esse. Numquam impedit assumenda non excepturi molestias modi. Odio 1460-02-01 autem atque occaecati. Ea mollitia consequuntur minima nesciunt natus. Inventore excepturi inventore culpa. Quam animi dolorum. Consectetur quo quam debitis nesciunt. A cum ipsa aspernatur labore voluptates sunt. Sequi recusandae molestiae ducimus.

1884-06-13 quidem voluptates repellendus 1368-06-21 blanditiis. Alias 1368-06-21 impedit. Quibusdam amet ea consequuntur explicabo. Quam dicta voluptatem excepturi doloremque veniam nihil. Corporis totam officiis pariatur. Eos dolorum minima doloribus ratione id nihil. Debitis veritatis dicta distinctio. Veniam ipsum eveniet corporis totam magnam. 1884-06-13 error earum numquam dolores. Provident 1117-05-14T16:43 facere magni aperiam. Eius perspiciatis nesciunt iure laudantium similique vero. Itaque magni ipsam impedit possimus cum. Veritatis vel saepe magni.

Impedit 1401-04-01 1401-04-01 1165-09-06. At dolor facilis laudantium sequi. Officiis temporibus 1401-04-01 adipisci dolores temporibus eius. Exercitationem ipsam reiciendis minus. Excepturi pariatur architecto odio fugiat nam. Perferendis 1401-04-01 suscipit. Neque cupiditate natus dolore recusandae.

Cumque distinctio occaecati laudantium voluptatum ea necessitatibus. Atque vitae numquam id soluta. Dicta illum at est est omnis voluptate earum. Odio illum similique aliquid ipsum modi. Illum vero temporibus enim minus. Maiores laborum aut soluta voluptatem. Asperiores doloribus assumenda quo. 1322-08-12T21:05 voluptatem voluptate soluta. Quo vero repudiandae minima 1946-02-14T11:29+19:30 voluptatem voluptas. Ab rem impedit aliquam 1865-09-02T11:02 fugit delectus.

Dolorum minus fuga officia accusamus possimus laudantium. Et fugiat quidem deleniti placeat corrupti eum. Quo cumque dignissimos. 1955-10-23T18:08+18:30 culpa placeat repellendus cum. Repudiandae alias molestias debitis. Porro vitae enim expedita error commodi doloremque perspiciatis. Dolorem sapiente quam iusto quibusdam sed distinctio delectus. Pariatur ratione suscipit nisi. Quia est doloribus inventore eos fugit. Laboriosam quos aspernatur ipsum animi.

Dolor vel cumque ipsum nisi praesentium. Aliquam praesentium illum quae 1700-12-09. Deserunt dolore explicabo 1002-02-02 nisi sapiente. Vero voluptas saepe omnis debitis sapiente. Ipsam autem inventore. Dolorem consectetur impedit adipisci.

Adipisci dolores similique nemo velit. Qui 1679-12-28 quod voluptatum dolorum sapiente voluptatibus. Soluta provident ullam velit debitis quis pariatur. Error suscipit ex dignissimos voluptates quasi similique. Vero vitae molestiae. Laborum minima culpa magnam. Repellendus esse molestiae quia eos repellat quia. Fuga reprehenderit tempore deleniti. Ea illum recusandae aliquam. Eius perspiciatis quas incidunt.

Quasi modi incidunt at nesciunt. Perspiciatis aliquam esse alias aut excepturi magni. Qui fugiat nostrum ipsum quae harum quis ex. Ipsam itaque error repellat libero. 1720-10-01 fugiat ipsum non culpa in quod. Eum iure provident eos repellat. Accusantium consequatur ut minus. Repudiandae deleniti quae odit. Dolore officia amet voluptatibus molestiae culpa. Illum placeat sed delectus voluptate iure.

Dicta possimus vel eaque. Incidunt harum vitae deserunt quam est. Iusto vitae modi provident. Cumque reiciendis provident cupiditate. Aut consequatur ad debitis. Possimus necessitatibus possimus tempora minus nemo. Error rerum ullam doloremque tempora libero reprehenderit eum. Cumque dolor praesentium amet eveniet aspernatur. Facilis porro ducimus pariatur veritatis vitae reprehenderit. Sequi quia velit maiores facilis fugiat voluptatibus. Quas consectetur assumenda nemo. Nisi quam excepturi nobis nobis facere tempore tempore.

Fugit consequatur cupiditate ducimus odio fuga. Expedita autem pariatur. Est optio mollitia error. Corrupti dolor tempora facilis enim modi. Dignissimos hic nobis laboriosam asperiores. Eligendi fugit placeat perspiciatis placeat ipsam error. Adipisci voluptate quasi enim ipsam odio magnam.

Doloremque dolores nihil neque iste. At doloremque neque ea dolor nesciunt. Exercitationem voluptates dolor dolores cupiditate vitae esse. Eos et fuga. Nemo sunt 1244-11-02 ullam. Neque voluptas dolor ratione exercitationem. Libero possimus possimus ipsam l1244-11-02ore. Magnam doloremque doloribus soluta eligendi ex.

Occaecati recusandae occaecati odit ut alias tempore. Repellat necessitatibus at eos aliquam. Sed quas corporis qui. Praesentium debitis eaque eius. Perferendis corrupti adipisci dolorum. Tempore consequuntur 1992-05-20 maiores aliquid harum. 1276-08-14 nisi vel similique id fuga. Quidem eos sunt eius. Eveniet commodi tempore qui autem perferendis nostrum.

Nobis dolore cum eligendi explicabo. 1594-08-05 ex commodi ea. Provident laboriosam dolorum quisquam magnam temporibus. 1594-08-05 error similique quaerat ab voluptates dolor. Debitis ullam vitae id unde officia. Reiciendis rem debitis dolor. Dolores sunt 1528-02-20T24:22 iste. Debitis et iure dolorum ratione deleniti. Id pariatur id doloribus possimus. Quaerat quia ea ad vitae odit. Beatae enim corporis assumenda distinctio optio. Earum aperiam laborum aliquid. Dolore deleniti at eveniet modi.

Error ipsam nisi. Excepturi modi doloremque iusto. Doloremque architecto quia minima voluptatem. Aliquam dolorum alias porro. Eos pariatur quis dignissimos ratione dolorum. Dicta a perspiciatis harum ipsam aperiam. Natus vel pariatur odit cupiditate. Aperiam assumenda quam 1254-05-04T05:28+22:00 accusantium voluptas placeat. Culpa esse 1074-01-18T09:43 exercitationem laborum repellendus enim.

Esse debitis delectus repudiandae. Voluptatem nesciunt iste consequatur vel dolores 1749-09-27. 1780-11-14 perferendis odio laboriosam. Perferendis harum repellendus qui nulla eos. Quos vero provident deleniti amet quasi. Hic voluptate quis eligendi.

Ipsum amet hic quidem tenetur. Sunt quod hic odit tenetur repellat voluptate 1672-06-28. Et ea quis libero odio 1995-12-24 officia. Voluptate velit reiciendis ducimus nesciunt eius. Nisi dignissimos necessitatibus totam necessitatibus asperiores. Tempore eaque harum deserunt. Deserunt temporibus consequuntur aut. Nisi repellendus eveniet repellat repellat possimus. Maiores ex natus accusantium autem necessitatibus. Labore hic error quidem ullam qui vel. Soluta vero aut. Tempore aut dolor commodi amet ratione autem quisquam. Laudantium voluptatibus dicta.

Enim illum distinctio incidunt. Modi ab odio vel minus delectus a natus. Quisquam ratione rerum accusamus vitae repudiandae. Nemo explicabo odio occaecati 1991-07-14T14:09+10:30 optio cumque. Cum sunt iusto rem accusamus accusantium. Minima illum occaecati enim 1982-02-03T10:11. Cumque nisi blanditiis vero doloribus dolores. Quibusdam dicta nobis. Ipsum consectetur culpa molestias consequuntur repudiandae.

Culpa architecto impedit sapiente assumenda consectetur voluptates. Repellendus consequuntur repellat mollitia. Accusantium aperiam saepe quos dolor culpa reiciendis. Esse corrupti non incidunt necessitatibus dolor eius inventore. Aut sapiente possimus 1699-05-31T05:32+24:00 quae. Occaecati nesciunt enim debitis quibusdam. 1650-08-01T04:24 modi ad deserunt explicabo. 1650-08-01T04:24 explicabo possimus inventore id. Veritatis veniam numquam doloribus harum quia. Expedita quod odit perferendis suscipit excepturi ad.
"""

regex = re.compile(r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})(?P<time>T\d{2}:\d{2}:\d{2})?(?P<timeZone>\d:\d)?")

parsedDates = []

for date in regex.finditer(entry):
  parsedDates.append(datetime.date(int(date.groupdict()['year']), int(date.groupdict()['month']), int(date.groupdict()['day'])))

birthday = datetime.date(2000, 7, 23)

birthdayDiffDates = []
for date in parsedDates:
    birthdayDiffDates.append(abs(birthday - date))

response = parsedDates[birthdayDiffDates.index(min(birthdayDiffDates))]

print("A data mais próxima do meu aniversário:", birthday, "é", response)
  