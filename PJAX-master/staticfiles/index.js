import Player from './player/lib.js';

new Player({
	target: '.my-player',
	delayPerSlide: 5,

	slides: [
		{
			url: '/static/img/chunk1.jpg',
			alt: 'slide1',

			filter: ['contrast(150%)', 'blur(5px)'],

			overlays: [
				{
					type: 'Text',
					text: 'Глэмпинг это очень здорово!',

					classes: ['watercolor'],

					styles: {
						'font-size': '40px',
						top: '30%',
						left: '20%'
					}
				},

				{
					type: 'Question',
					question: 'Вы со мной согласны?',

					variants: [
						'Да',
						'Нет'
					],

					styles: {
						top: '60%',
						left: '30%'
					}
				}
			]
		},

		{
			url: '/static/img/chunk2.jpg',
			alt: 'slide2',

			overlays: [
				{
					type: 'Text',
					text: 'Миру - мир! Любовь и радуга!',

					classes: ['watercolor'],

					styles: {
						top: '50%',
						left: '10%'
					}
				}
			]
		},

		{
			url: '/static/img/chunk3.jpg',
			alt: 'slide3',

			overlays: [
				{
					type: 'Text',
					text: 'Пейте чистую воду!',

					classes: ['watercolor'],

					styles: {
						'font-size': '20px',
						top: '50%',
						left: '10%'
					}
				}
			]
		},

		{url: '/static/img/chunk4.jpg', alt: 'slide4'}
	]
})
