class DocumentInfos:

    title = u'Problème du voyageur de commerce'
    first_name = 'Julien'
    last_name = 'Grandchamp'
    author = f'{first_name} {last_name}'
    year = u'2023'
    month = u'Janvier'
    seminary_title = u'Travail personnel OCI'
    tutor = u"Cédric Donner"
    release = "(Version finale)"
    repository_url = "https://github.com/julienGrandchamp/Probleme-du-voyageur-de-commerce"

    @classmethod
    def date(cls):
        return cls.month + " " + cls.year

infos = DocumentInfos()