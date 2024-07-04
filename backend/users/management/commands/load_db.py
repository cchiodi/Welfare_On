from django.core.management.base import BaseCommand
from django.apps import apps

class Command(BaseCommand):
	help = 'Load data into the database'


	def handle(self, *args, **options):
		self.generate_superuser()
		self.create_initial_data()


	def generate_superuser(self):
		User = apps.get_model('users', 'User')
		if not User.objects.filter(username='admin').exists():
			User.objects.create_superuser(
				username='admin',
				email='admin@example.com',
				password='admin'
			)
			self.stdout.write(self.style.SUCCESS('Successfully created superuser'))


	def create_categories_and_subcategories(self, Category, Subcategory):
		categories = [
			{
				'name': 'Benessere Economico',
				'color': '#FF5733',
				'subcategories': [
					'Formazione e Workshop',
					'Assicurazioni',
					'Shopping e Servizi Online']
			},
			{
				'name': 'Benessere Familiare',
				'color': '#33FF57',
				'subcategories': [
					'Viaggi e Trasporti',
					'Eventi Musicali e Spettacoli',
					'Supporto Psicologico e Familiare']
			},
			{
				'name': 'Benessere Psicologico',
				'color': '#33FF57',
				'subcategories': [
					'Libri e eBooks',
					'Arte e Cultura',
					'Miglioramento Personale']
			},
			{
				'name': 'Benessere Fisico',
				'color': '#3357FF',
				'subcategories': [
					'Fitness e Benessere',
					'Mobilità Sostenibile',
					'Eventi Sportivi']
			},
		]

		for category_data in categories:
			category, created = Category.objects.get_or_create(
				name=category_data['name'],
				color=category_data['color'])
			if created:
				self.stdout.write(self.style.SUCCESS(f'Created category {category.name}'))
			for subcategory_name in category_data['subcategories']:
				subcategory, sub_created = Subcategory.objects.get_or_create(
					name=subcategory_name,
					category=category)
				if sub_created:
					self.stdout.write(self.style.SUCCESS(f'Created subcategory {subcategory.name}'))


	def create_interests(self, Interest):
		interests = [
			'Cosmetica', 'Abbigliamento e Accessori', 'Cinema', 'Eventi sportivi', 'Teatro e Spettacoli',
			'Psicologia e Supporto', 'Noleggio e Trasporti', 'Miglioramento Personale', 'Investimento e Benefits',
			'Libri e eBooks', 'Musei e Arte', 'Vacanze e Viaggi', 'Palestra e Fitness', 'Salute e Benessere',
			'Musica e Concerti', 'Mobilità sostenibile', 'Motori', 'Orologi di lusso', 'Famiglia e Bambini',
			'Formazione e Workshop'
		]

		for interest_name in interests:
			Interest.objects.get_or_create(name=interest_name)


	def create_services(self, Service, Subcategory, Interest):
		services = [
			{
				'name': 'Alitalia',
				'data_start': '2024-06-26',
				'data_end': '2024-07-26',
				'description': 'Alitalia offre uno sconto del 15% sui voli in classe Business. Approfitta di questa promozione per godere di comfort superiore, accesso a lounge esclusive e pasti gourmet. Ideale per viaggi di lavoro o per chi cerca un\'esperienza di volo lussuosa, questa offerta consente di viaggiare con stile e risparmiare.',
				'img_url': 'http://localhost:5000/admin/users/service/add/',
				'pdf_url': 'http://localhost:5000/admin/users/service/add/',
				'subcategory': 'Viaggi e Trasporti',
				'interests': ['Vacanze e Viaggi']
			},
			{
				'name': 'MSC Crociere',
				'data_start': '2024-06-26',
				'data_end': '2024-07-26',
				'description': 'MSC Crociere offre uno sconto del 10% sulle crociere da e per la Sicilia. Approfitta di questa promozione per vivere un’esperienza indimenticabile in mare, con servizi di alta qualità e itinerari affascinanti. Goditi il massimo del comfort e del divertimento a bordo delle navi MSC.',
				'img_url': 'http://localhost:5000/admin/users/service/add/',
				'pdf_url': 'http://localhost:5000/admin/users/service/add/',
				'subcategory': 'Viaggi e Trasporti',
				'interests': ['Vacanze e Viaggi']
			},
			{
				'name': 'Trenitalia',
				'data_start': '2024-06-26',
				'data_end': '2024-07-26',
				'description': 'Trenitalia offre uno sconto del 15% sui biglietti Frecce in classe Executive. Viaggia con comfort e servizi premium, tra cui sedili reclinabili e connessione Wi-Fi gratuita. Ideale per chi cerca un viaggio in treno di alta qualità a un prezzo scontato.',
				'img_url': 'http://localhost:5000/admin/users/service/add/',
				'pdf_url': 'http://localhost:5000/admin/users/service/add/',
				'subcategory': 'Viaggi e Trasporti',
				'interests': ['Vacanze e Viaggi']
			},
			{
				'name': 'Novotel',
				'data_start': '2024-06-26',
				'data_end': '2024-07-26',
				'description': 'Novotel offre uno sconto del 15% sui soggiorni nei suoi alberghi. Approfitta di questa promozione per goderti una vacanza o un viaggio di lavoro con tutti i comfort moderni. Novotel garantisce servizi eccellenti e un\'ospitalità di alto livello a un prezzo conveniente.',
				'img_url': 'http://localhost:5000/admin/users/service/add/',
				'pdf_url': 'http://localhost:5000/admin/users/service/add/',
				'subcategory': 'Viaggi e Trasporti',
				'interests': ['Vacanze e Viaggi']
			},
			{
				'name': 'UnipolSai',
				'data_start': '2024-06-26',
				'data_end': '2024-07-26',
				'description': 'UnipolSai offre un\'opportunità imperdibile per risparmiare sulle assicurazioni auto e moto. Con uno sconto del 10%, puoi ottenere una copertura completa per i tuoi veicoli, garantendo protezione e tranquillità su strada. Approfitta di questa offerta per ridurre i costi assicurativi e viaggiare in sicurezza.',
				'img_url': 'http://localhost:5000/admin/users/service/add/',
				'pdf_url': 'http://localhost:5000/admin/users/service/add/',
				'subcategory': 'Assicurazioni',
				'interests': ['Motori']
			},
			{
				'name': 'Cattolica',
				'data_start': '2024-06-26',
				'data_end': '2024-07-26',
				'description': 'Cattolica Assicurazioni propone un\'importante promozione sulla polizza vita, offrendo uno sconto del 25%. Questa polizza è ideale per chi desidera garantire un futuro sereno ai propri cari, con una protezione finanziaria robusta in caso di eventi imprevisti. Scegli Cattolica per un\'assicurazione vita affidabile e conveniente.',
				'img_url': 'http://localhost:5000/admin/users/service/add/',
				'pdf_url': 'http://localhost:5000/admin/users/service/add/',
				'subcategory': 'Assicurazioni',
				'interests': ['Investimento e Benefits']
			},
			{
				'name': 'AXA Assicurazioni',
				'data_start': '2024-06-26',
				'data_end': '2024-07-26',
				'description': 'AXA offre uno sconto del 20% sulle assicurazioni viaggi, perfetto per chi ama esplorare il mondo senza pensieri. La polizza copre spese mediche, annullamento del viaggio, smarrimento bagagli e molto altro. Viaggia in sicurezza e risparmia con AXA, la tua compagna di fiducia in ogni avventura.',
				'img_url': 'http://localhost:5000/admin/users/service/add/',
				'pdf_url': 'http://localhost:5000/admin/users/service/add/',
				'subcategory': 'Assicurazioni',
				'interests': ['Vacanze e Viaggi']
			},
			{
				'name': 'UniSanitaria',
				'data_start': '2024-06-26',
				'data_end': '2024-07-26',
				'description': 'UniSanitaria propone un\'offerta imperdibile con uno sconto del 30% sulle polizze sanitarie. Questa promozione è pensata per chi desidera avere un accesso rapido e garantito a cure mediche di alta qualità. La polizza copre visite specialistiche, esami diagnostici, ricoveri e interventi chirurgici. Scegli UniSanitaria per la tua salute.',
				'img_url': 'http://localhost:5000/admin/users/service/add/',
				'pdf_url': 'http://localhost:5000/admin/users/service/add/',
				'subcategory': 'Assicurazioni',
				'interests': ['Salute e Benessere']
			},
			{
				'name': 'Emma Marrone Tour Estivo',
				'data_start': '2024-06-26',
				'data_end': '2024-07-26',
				'description': 'Gli appassionati di musica hanno un motivo in più per gioire con uno sconto del 10% sui biglietti del Tour Estivo di Emma Marrone. Non perdere l\'occasione di assistere a uno spettacolo emozionante e coinvolgente, godendo delle performance dal vivo di una delle artiste più amate in Italia. Acquista subito i tuoi biglietti.',
				'img_url': 'http://localhost:5000/admin/users/service/add/',
				'pdf_url': 'http://localhost:5000/admin/users/service/add/',
				'subcategory': 'Eventi Musicali e Spettacoli',
				'interests': ['Musica e Concerti']
			},
			{
				'name': 'Workshop Web3 e Blockchain',
				'data_start': '2024-06-26',
				'data_end': '2024-07-26',
				'description': 'Partecipa al Workshop Web3 e Blockchain questo sabato con uno sconto del 20%. Questo evento formativo, previsto per l\'intera giornata, è dedicato a chi vuole approfondire le conoscenze sulle tecnologie emergenti del Web3 e della Blockchain. Esperti del settore guideranno sessioni interattive, offrendo strumenti pratici e conoscenze avanzate.',
				'img_url': 'http://localhost:5000/admin/users/service/add/',
				'pdf_url': 'http://localhost:5000/admin/users/service/add/',
				'subcategory': 'Formazione e Workshop',
				'interests': ['Formazione e Workshop']
			},
			{
				'name': 'La Metamorfosi di Kafka',
				'data_start': '2024-06-26',
				'data_end': '2024-07-26',
				'description': 'Approfitta dello sconto del 20% sull\'ebook de "La Metamorfosi" di Franz Kafka. Un classico della letteratura che racconta la surreale trasformazione di Gregor Samsa, esplorando temi di alienazione e identità. Una lettura imprescindibile per gli amanti della narrativa profonda e riflessiva. Disponibile ora a un prezzo scontato.',
				'img_url': 'http://localhost:5000/admin/users/service/add/',
				'pdf_url': 'http://localhost:5000/admin/users/service/add/',
				'subcategory': 'Libri e eBooks',
				'interests': ['Libri e eBooks']
			},
			{
				'name': 'WellHUB Pilates Flex',
				'data_start': '2024-06-26',
				'data_end': '2024-07-26',
				'description': 'Unisciti al corso di Pilates Flex stasera alle ore 19.00 per migliorare la tua flessibilità, forza e postura. Questo corso è adatto a tutti i livelli e guidato da istruttori esperti che ti aiuteranno a raggiungere i tuoi obiettivi di fitness in un ambiente accogliente e motivante. Prenota il tuo posto e inizia il tuo percorso di benessere.',
				'img_url': 'http://localhost:5000/admin/users/service/add/',
				'pdf_url': 'http://localhost:5000/admin/users/service/add/',
				'subcategory': 'Fitness e Benessere',
				'interests': ['Palestra e Fitness']
			},
			{
				'name': 'WellHUB Crossfit',
				'data_start': '2024-06-26',
				'data_end': '2024-07-26',
				'description': 'Partecipa al corso di Crossfit stasera alle ore 20.00 per un allenamento intenso che combina sollevamento pesi, cardio e movimenti funzionali. Ideale per chi cerca una sfida e vuole migliorare la propria forma fisica generale. Gli istruttori certificati ti guideranno attraverso ogni esercizio, garantendo un\'esperienza sicura ed efficace.',
				'img_url': 'http://localhost:5000/admin/users/service/add/',
				'pdf_url': 'http://localhost:5000/admin/users/service/add/',
				'subcategory': 'Fitness e Benessere',
				'interests': ['Palestra e Fitness']
			},
			{
				'name': 'Internazionali BNL',
				'data_start': '2024-06-26',
				'data_end': '2024-07-26',
				'description': 'Gli appassionati di tennis possono beneficiare di uno sconto del 15% sui biglietti per gli Internazionali BNL. Questo prestigioso torneo attira i migliori giocatori del mondo e offre spettacoli di altissimo livello. Non perdere l\'opportunità di vedere dal vivo match emozionanti e godere di un\'atmosfera sportiva unica.',
				'img_url': 'http://localhost:5000/admin/users/service/add/',
				'pdf_url': 'http://localhost:5000/admin/users/service/add/',
				'subcategory': 'Eventi Sportivi',
				'interests': ['Eventi Sportivi']
			},
			{
				'name': 'Galleria Borghese',
				'data_start': '2024-06-26',
				'data_end': '2024-07-26',
				'description': 'Visita la Galleria Borghese con uno sconto del 15%. Questo museo ospita una collezione straordinaria di opere d\'arte, tra cui capolavori di Caravaggio, Bernini e Raffaello. Un\'occasione imperdibile per ammirare arte e cultura in uno dei luoghi più affascinanti di Roma. Prenota i tuoi biglietti scontati e immergiti nella bellezza.',
				'img_url': 'http://localhost:5000/admin/users/service/add/',
				'pdf_url': 'http://localhost:5000/admin/users/service/add/',
				'subcategory': 'Arte e Cultura',
				'interests': ['Musei e Arte']
			},
			{
				'name': 'NowTV',
				'data_start': '2024-06-26',
				'data_end': '2024-07-26',
				'description': 'Abbonati a NowTV con uno sconto del 20% e goditi una vasta gamma di film, serie TV, documentari e programmi sportivi. Un\'ottima opportunità per gli amanti dell\'intrattenimento che vogliono accedere a contenuti premium a un prezzo conveniente. Scopri tutte le novità e gli show più popolari con NowTV.',
				'img_url': 'http://localhost:5000/admin/users/service/add/',
				'pdf_url': 'http://localhost:5000/admin/users/service/add/',
				'subcategory': 'Shopping e Servizi Online',
				'interests': ['Cinema']
			},
			{
				'name': 'Ludovico Einaudi Tour Italiano',
				'data_start': '2024-06-26',
				'data_end': '2024-07-26',
				'description': 'Non perdere l\'occasione di assistere al Tour Italiano di Ludovico Einaudi con uno sconto del 15% sui biglietti. Il celebre pianista e compositore ti porterà in un viaggio musicale emozionante con le sue composizioni uniche e toccanti. Acquista i tuoi biglietti scontati e vivi un\'esperienza musicale indimenticabile.',
				'img_url': 'http://localhost:5000/admin/users/service/add/',
				'pdf_url': 'http://localhost:5000/admin/users/service/add/',
				'subcategory': 'Eventi Musicali e Spettacoli',
				'interests': ['Musica e Concerti']
			},
			{
				'name': 'Don Chisciotte Teatro San Carlo',
				'data_start': '2024-06-26',
				'data_end': '2024-07-26',
				'description': 'Goditi lo spettacolo di "Don Chisciotte" al Teatro San Carlo con uno sconto del 10%. Questa rappresentazione teatrale offre una rivisitazione moderna del classico di Cervantes, combinando elementi di danza, recitazione e musica. Un\'esperienza culturale unica per tutti gli amanti del teatro.',
				'img_url': 'http://localhost:5000/admin/users/service/add/',
				'pdf_url': 'http://localhost:5000/admin/users/service/add/',
				'subcategory': 'Eventi Musicali e Spettacoli',
				'interests': ['Teatro e Spettacoli']
			},
			# {
			# 	'name': 'UciCinema',
			# 	'data_start': '2024-06-26',
			# 	'data_end': '2024-07-26',
			# 	'description': 'UciCinema propone uno sconto del 25% per le famiglie. Un\'occasione perfetta per trascorrere una serata al cinema con i propri cari, godendo dei film più recenti e di un ambiente confortevole. Approfitta di questa offerta per un\'esperienza cinematografica indimenticabile con tutta la famiglia.',
			# 	'img_url': 'http://localhost:5000/admin/users/service/add/',
			# 	'pdf_url': 'http://localhost:5000/admin/users/service/add/',
			# 	'subcategory': 'Cinema e Intrattenimento',
			# 	'interests': ['Famiglia e Bambini']
			# },
			{
				'name': 'Autoscout Volvo XC70',
				'data_start': '2024-06-26',
				'data_end': '2024-07-26',
				'description': 'Se sei in cerca di un\'auto, Autoscout offre uno sconto del 10% su una selezione di modelli Volvo XC70. Questi veicoli sono noti per la loro robustezza, comfort e prestazioni eccellenti. Un\'opportunità imperdibile per acquistare un\'auto di qualità a un prezzo ridotto.',
				'img_url': 'http://localhost:5000/admin/users/service/add/',
				'pdf_url': 'http://localhost:5000/admin/users/service/add/',
				'subcategory': 'Mobilità Sostenibile',
				'interests': ['Motori']
			},
			{
				'name': 'InMoto',
				'data_start': '2024-06-26',
				'data_end': '2024-07-26',
				'description': 'InMoto offre uno sconto del 5% su moto usate. Questa promozione è ideale per gli appassionati di motociclismo che cercano un mezzo affidabile e conveniente. Scopri la vasta gamma di moto disponibili e approfitta di questa offerta per risparmiare sull\'acquisto della tua prossima due ruote.',
				'img_url': 'http://localhost:5000/admin/users/service/add/',
				'pdf_url': 'http://localhost:5000/admin/users/service/add/',
				'subcategory': 'Mobilità Sostenibile',
				'interests': ['Motori']
			},
			{
				'name': 'Cooltra',
				'data_start': '2024-06-26',
				'data_end': '2024-07-26',
				'description': 'Noleggia uno scooter con Cooltra e ottieni uno sconto del 20%. Questa offerta è perfetta per chi cerca un modo pratico ed economico per muoversi in città. Cooltra offre una vasta gamma di scooter moderni e ben mantenuti. Approfitta di questa promozione per un trasporto veloce e conveniente.',
				'img_url': 'http://localhost:5000/admin/users/service/add/',
				'pdf_url': 'http://localhost:5000/admin/users/service/add/',
				'subcategory': 'Mobilità Sostenibile',
				'interests': ['Noleggio e Trasporti']
			},
			{
				'name': 'Leasys',
				'data_start': '2024-06-26',
				'data_end': '2024-07-26',
				'description': 'Leasys propone un\'opzione di noleggio a lungo termine senza anticipo. Questa offerta è ideale per chi desidera guidare un\'auto nuova senza i costi iniziali elevati. Leasys offre una vasta gamma di veicoli, piani flessibili e servizi inclusi per una soluzione di mobilità conveniente e senza pensieri.',
				'img_url': 'http://localhost:5000/admin/users/service/add/',
				'pdf_url': 'http://localhost:5000/admin/users/service/add/',
				'subcategory': 'Mobilità Sostenibile',
				'interests': ['Noleggio e Trasporti']
			},
			{
				'name': 'EuropCar',
				'data_start': '2024-06-26',
				'data_end': '2024-07-26',
				'description': 'EuropCar offre uno sconto del 15% sul noleggio di auto. Questa promozione è perfetta per chi necessita di un veicolo per un breve periodo, sia per viaggi di lavoro che di piacere. EuropCar garantisce una flotta moderna e diversificata, con opzioni per tutte le esigenze. Approfitta di questa offerta per un noleggio conveniente.',
				'img_url': 'http://localhost:5000/admin/users/service/add/',
				'pdf_url': 'http://localhost:5000/admin/users/service/add/',
				'subcategory': 'Mobilità Sostenibile',
				'interests': ['Noleggio e Trasporti']
			},
			{
				'name': 'Autodoc.it',
				'data_start': '2024-06-26',
				'data_end': '2024-07-26',
				'description': 'Acquista articoli selezionati su Autodoc.it con uno sconto del 15%. Questa offerta è ideale per chi cerca ricambi e accessori per auto di alta qualità a prezzi scontati. Autodoc.it offre una vasta gamma di prodotti delle migliori marche. Non perdere l\'occasione di risparmiare sulla manutenzione del tuo veicolo.',
				'img_url': 'http://localhost:5000/admin/users/service/add/',
				'pdf_url': 'http://localhost:5000/admin/users/service/add/',
				'subcategory': 'Mobilità Sostenibile',
				'interests': ['Noleggio e Trasporti']
			},
			{
				'name': 'Leonardo Summer Camp',
				'data_start': '2024-06-26',
				'data_end': '2024-07-26',
				'description': 'Iscrivi i tuoi figli al Leonardo Summer Camp per un\'esperienza estiva educativa e divertente. Questo camp offre una varietà di attività sportive, creative e formative, progettate per stimolare la curiosità e lo sviluppo dei bambini. Un\'opportunità perfetta per un\'estate indimenticabile.',
				'img_url': 'http://localhost:5000/admin/users/service/add/',
				'pdf_url': 'http://localhost:5000/admin/users/service/add/',
				'subcategory': 'Supporto Psicologico e Familiare',
				'interests': ['Famiglia e Bambini']
			},
			{
				'name': 'Prenatal',
				'data_start': '2024-06-26',
				'data_end': '2024-07-26',
				'description': 'Prenatal offre un ulteriore sconto del 15% per i possessori della carta VIP. Questa promozione è ideale per le famiglie in crescita, che possono acquistare prodotti per neonati, bambini e mamme a prezzi ancora più vantaggiosi. Scopri la qualità e la convenienza dei prodotti Prenatal con questo sconto esclusivo.',
				'img_url': 'http://localhost:5000/admin/users/service/add/',
				'pdf_url': 'http://localhost:5000/admin/users/service/add/',
				'subcategory': 'Shopping e Servizi Online',
				'interests': ['Famiglia e Bambini']
			},
			{
				'name': 'Palestre',
				'data_start': '2024-06-26',
				'data_end': '2024-07-26',
				'description': 'Scopri le palestre partner e trova la struttura perfetta per tutta la famiglia. Queste palestre offrono una vasta gamma di attività e corsi per tutte le età e livelli di fitness. Che tu voglia fare esercizio fisico, partecipare a lezioni di gruppo o rilassarti in un ambiente accogliente, troverai la soluzione giusta per te e i tuoi cari.',
				'img_url': 'http://localhost:5000/admin/users/service/add/',
				'pdf_url': 'http://localhost:5000/admin/users/service/add/',
				'subcategory': 'Fitness e Benessere',
				'interests': ['Palestra e Fitness']
			},
			{
				'name': 'Caregivers',
				'data_start': '2024-06-26',
				'data_end': '2024-07-26',
				'description': 'Scopri la rete di Caregiver per anziani e persone in necessità, un servizio pensato per offrire assistenza e supporto qualificato a chi ne ha bisogno. I caregiver sono professionisti esperti che garantiscono cure personalizzate, migliorando la qualità della vita degli assistiti e delle loro famiglie. Affidati a questo servizio per un aiuto prezioso.',
				'img_url': 'http://localhost:5000/admin/users/service/add/',
				'pdf_url': 'http://localhost:5000/admin/users/service/add/',
				'subcategory': 'Supporto Psicologico e Familiare',
				'interests': ['Famiglia e Bambini']
			},
			{
				'name': 'Sephora Milano',
				'data_start': '2024-06-26',
				'data_end': '2024-07-26',
				'description': 'Sephora Milano offre uno sconto del 10% su una vasta gamma di prodotti di bellezza. Approfitta di questa promozione per acquistare i tuoi cosmetici preferiti, prodotti per la cura della pelle e accessori di tendenza. Sephora è sinonimo di qualità e innovazione nel mondo della bellezza. Non perdere questa occasione per risparmiare.',
				'img_url': 'http://localhost:5000/admin/users/service/add/',
				'pdf_url': 'http://localhost:5000/admin/users/service/add/',
				'subcategory': 'Shopping e Servizi Online',
				'interests': ['Cosmetica']
			},
			{
				'name': 'QC terme',
				'data_start': '2024-06-26',
				'data_end': '2024-07-26',
				'description': 'Concediti un\'esperienza di relax totale con QC Terme, che offre uno sconto del 20%. Goditi trattamenti termali, massaggi e percorsi benessere in un ambiente elegante e tranquillo. Questa offerta è ideale per chi desidera staccare dalla routine quotidiana e rigenerarsi. Prenota il tuo trattamento scontato e vivi un momento di puro piacere.',
				'img_url': 'http://localhost:5000/admin/users/service/add/',
				'pdf_url': 'http://localhost:5000/admin/users/service/add/',
				'subcategory': 'Fitness e Benessere',
				'interests': ['Salute e Benessere']
			},
			{
				'name': 'YOOX',
				'data_start': '2024-06-26',
				'data_end': '2024-07-26',
				'description': 'Fai shopping su YOOX con uno sconto del 15% e scopri una selezione esclusiva di abbigliamento, accessori e calzature. YOOX offre prodotti di brand famosi e designer emergenti, garantendo stile e qualità. Approfitta di questa promozione per rinnovare il tuo guardaroba con pezzi unici e alla moda.',
				'img_url': 'http://localhost:5000/admin/users/service/add/',
				'pdf_url': 'http://localhost:5000/admin/users/service/add/',
				'subcategory': 'Shopping e Servizi Online',
				'interests': ['Abbigliamento e Accessori']
			},
			{
				'name': 'Chrono24',
				'data_start': '2024-06-26',
				'data_end': '2024-07-26',
				'description': 'Chrono24 offre uno sconto del 15% su articoli selezionati. Questa piattaforma è ideale per gli appassionati di orologi di lusso, offrendo una vasta gamma di modelli nuovi e usati delle marche più prestigiose. Non perdere l\'occasione di acquistare il tuo orologio da sogno a un prezzo scontato.',
				'img_url': 'http://localhost:5000/admin/users/service/add/',
				'pdf_url': 'http://localhost:5000/admin/users/service/add/',
				'subcategory': 'Shopping e Servizi Online',
				'interests': ['Orologi di lusso']
			},
			{
				'name': 'Off-Market.com',
				'data_start': '2024-06-26',
				'data_end': '2024-07-26',
				'description': 'Off-Market.com propone uno sconto del 35% su articoli firmati selezionati. Questa offerta è perfetta per chi cerca capi di alta moda a prezzi ridotti. Scopri le collezioni dei brand più rinomati e approfitta di questa promozione per aggiungere un tocco di eleganza al tuo guardaroba.',
				'img_url': 'http://localhost:5000/admin/users/service/add/',
				'pdf_url': 'http://localhost:5000/admin/users/service/add/',
				'subcategory': 'Shopping e Servizi Online',
				'interests': ['Abbigliamento e Accessori']
			},
			{
				'name': 'GrandVision',
				'data_start': '2024-06-26',
				'data_end': '2024-07-26',
				'description': 'GrandVision offre uno sconto del 15% su montature e occhiali da vista. Approfitta di questa promozione per acquistare occhiali di alta qualità e stile. Con una vasta gamma di modelli e marchi disponibili, troverai sicuramente la montatura perfetta per le tue esigenze. Migliora la tua visione con GrandVision.',
				'img_url': 'http://localhost:5000/admin/users/service/add/',
				'pdf_url': 'http://localhost:5000/admin/users/service/add/',
				'subcategory': 'Shopping e Servizi Online',
				'interests': ['Salute e Benessere']
			},
			{
				'name': 'Nike.com',
				'data_start': '2024-06-26',
				'data_end': '2024-07-26',
				'description': 'Acquista su Nike.com con uno sconto del 15% su tutta la linea Sportswear. Questa offerta è ideale per gli appassionati di sport che cercano abbigliamento e accessori di alta qualità. Scopri le ultime collezioni e i prodotti innovativi di Nike, progettati per migliorare le tue prestazioni atletiche.',
				'img_url': 'http://localhost:5000/admin/users/service/add/',
				'pdf_url': 'http://localhost:5000/admin/users/service/add/',
				'subcategory': 'Shopping e Servizi Online',
				'interests': ['Abbigliamento e Accessori']
			},
			{
				'name': 'Zalando.it',
				'data_start': '2024-06-26',
				'data_end': '2024-07-26',
				'description': 'Zalando offre uno sconto del 25% su articoli selezionati. Approfitta di questa promozione per acquistare abbigliamento, calzature e accessori delle migliori marche a prezzi ridotti. Zalando è sinonimo di stile e qualità, con una vasta gamma di prodotti per ogni gusto e occasione.',
				'img_url': 'http://localhost:5000/admin/users/service/add/',
				'pdf_url': 'http://localhost:5000/admin/users/service/add/',
				'subcategory': 'Shopping e Servizi Online',
				'interests': ['Abbigliamento e Accessori']
			},
			{
				'name': 'Flexible Benefits AON',
				'data_start': '2024-06-26',
				'data_end': '2024-07-26',
				'description': 'Scopri il programma Flexible Benefits di AON, che offre una gamma completa di servizi e vantaggi per i dipendenti. Dal benessere fisico e mentale alla formazione professionale, questo programma è progettato per migliorare la qualità della vita e il bilancio tra lavoro e vita privata. Esplora tutte le opzioni disponibili e sfrutta al meglio i benefici offerti.',
				'img_url': 'http://localhost:5000/admin/users/service/add/',
				'pdf_url': 'http://localhost:5000/admin/users/service/add/',
				'subcategory': 'Supporto Psicologico e Familiare',
				'interests': ['Investimento e Benefits']
			},
			{
				'name': 'Fineco',
				'data_start': '2024-06-26',
				'data_end': '2024-07-26',
				'description': 'Scopri i Piani di Accumulo del Capitale (PAC) e i Piani di Rimborso programmato di Fineco. Questi strumenti finanziari sono ideali per chi desidera investire in modo sistematico e ottenere rendimenti nel lungo termine. Fineco offre soluzioni personalizzate e un supporto esperto per aiutarti a raggiungere i tuoi obiettivi finanziari.',
				'img_url': 'http://localhost:5000/admin/users/service/add/',
				'pdf_url': 'http://localhost:5000/admin/users/service/add/',
				'subcategory': 'Supporto Psicologico e Familiare',
				'interests': ['Investimento e Benefits']
			},
			{
				'name': 'Leonardo Benefits: mutui e prestiti agevolati',
				'data_start': '2024-06-26',
				'data_end': '2024-07-26',
				'description': 'Leonardo offre una sezione dedicata ai mutui e prestiti agevolati per i suoi dipendenti. Questa iniziativa è pensata per facilitare l\'accesso al credito a condizioni vantaggiose, supportando le esigenze finanziarie dei lavoratori. Scopri tutte le opzioni disponibili e scegli la soluzione più adatta per te.',
				'img_url': 'http://localhost:5000/admin/users/service/add/',
				'pdf_url': 'http://localhost:5000/admin/users/service/add/',
				'subcategory': 'Supporto Psicologico e Familiare',
				'interests': ['Investimento e Benefits']
			},
			{
				'name': 'Apertamente',
				'data_start': '2024-06-26',
				'data_end': '2024-07-26',
				'description': 'Leonardo mette a disposizione un team di psicologi per supporto in presenza o a distanza. Questo servizio è pensato per offrire assistenza psicologica professionale, migliorando il benessere mentale e la qualità della vita dei dipendenti. Scopri come accedere al servizio e beneficiare di un supporto esperto e dedicato.',
				'img_url': 'http://localhost:5000/admin/users/service/add/',
				'pdf_url': 'http://localhost:5000/admin/users/service/add/',
				'subcategory': 'Supporto Psicologico e Familiare',
				'interests': ['Psicologia e Supporto']
			},
			{
				'name': 'Leader di te stesso di Roberto Re',
				'data_start': '2024-06-26',
				'data_end': '2024-07-26',
				'description': 'Leonardo mette a disposizione un team di psicologi per supporto in presenza o a distanza. Questo servizio è pensato per offrire assistenza psicologica professionale, migliorando il benessere mentale e la qualità della vita dei dipendenti. Scopri come accedere al servizio e beneficiare di un supporto esperto e dedicato.',
				'img_url': 'http://localhost:5000/admin/users/service/add/',
				'pdf_url': 'http://localhost:5000/admin/users/service/add/',
				'subcategory': 'Formazione e Workshop',
				'interests': ['Miglioramento Personale']
			},
			{
				'name': 'JoJob',
				'data_start': '2024-06-26',
				'data_end': '2024-07-26',
				'description': 'Scopri l\'app JoJob per il carpooling Casa-Lavoro e connettiti con i tuoi colleghi per viaggi condivisi. Questa app è progettata per ridurre le emissioni di CO2, risparmiare sui costi di trasporto e favorire la socializzazione tra colleghi. Unisciti alla comunità di JoJob e contribuisci a un ambiente più sostenibile.',
				'img_url': 'http://localhost:5000/admin/users/service/add/',
				'pdf_url': 'http://localhost:5000/admin/users/service/add/',
				'subcategory': 'Mobilità Sostenibile',
				'interests': ['Noleggio e Trasporti']
			},
			{
				'name': 'Autoscout Fiat 500e',
				'data_start': '2024-06-26',
				'data_end': '2024-07-26',
				'description': 'Autoscout offre uno sconto del 10% sulla FIAT 500e full electric. Questa offerta è ideale per chi desidera passare a un veicolo elettrico, combinando efficienza energetica e stile. La 500e è una scelta ecologica che offre un\'esperienza di guida silenziosa e a basse emissioni. Approfitta dello sconto per un futuro più green.',
				'img_url': 'http://localhost:5000/admin/users/service/add/',
				'pdf_url': 'http://localhost:5000/admin/users/service/add/',
				'subcategory': 'Mobilità Sostenibile',
				'interests': ['Motori']
			},
			{
				'name': 'Corsi di Tennis e Padel',
				'data_start': '2024-06-26',
				'data_end': '2024-07-26',
				'description': 'Approfitta di uno sconto del 15% sui corsi di Tennis e Padel. Questa offerta è perfetta per gli appassionati di sport che vogliono migliorare le proprie abilità e divertirsi. I corsi sono tenuti da istruttori esperti e adatti a tutti i livelli di abilità. Iscriviti ora e goditi il divertimento e l\'allenamento con uno sconto speciale.',
				'img_url': 'http://localhost:5000/admin/users/service/add/',
				'pdf_url': 'http://localhost:5000/admin/users/service/add/',
				'subcategory': 'Eventi Sportivi',
				'interests': ['Eventi sportivi']
			},
		]

		for service_data in services:
			subcategory = Subcategory.objects.get(
				name=service_data['subcategory'])
			service, created = Service.objects.get_or_create(
				name=service_data['name'],
				data_start=service_data['data_start'],
				data_end=service_data['data_end'],
				description=service_data['description'],
				img_url=service_data['img_url'],
				pdf_url=service_data['pdf_url'],
				subcategory=subcategory
			)
			if created:
				self.stdout.write(self.style.SUCCESS(f'Created service {service.name}'))
			service.interests.set(Interest.objects.filter(
				name__in=service_data['interests']))


	def create_initial_data(self):
		Category = apps.get_model('categories', 'Category')
		Subcategory = apps.get_model('categories', 'Subcategory')
		Interest = apps.get_model('interests', 'Interest')
		Service = apps.get_model('services', 'Service')

		self.create_categories_and_subcategories(Category, Subcategory)
		self.create_interests(Interest)
		self.create_services(Service, Subcategory, Interest)
		self.stdout.write(self.style.SUCCESS('Successfully created categories, subcategories, interests and services'))
