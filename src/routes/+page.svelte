<script lang="ts">
	import { lang } from '$lib/stores';
	const content = {
		gallery: { en: 'Gallery', ru: 'Галерея' },
		cont: { en: 'of contemprorary', ru: 'сoвременного' },
		art: { en: 'art', ru: 'искусства' },
		opened: {
			en: 'Opened in december 2020',
			ru: 'Открыта в декабре 2020 года'
		},
		andnow: {
			en: 'Since march 2022 exists only in virtual space',
			ru: 'С марта 2022 года находится только в виртуальном пространстве'
		}
	};
</script>

<section class="main-section">
	<div class="subsection p-10 pl-20 items-center flex">
		<h4>
			{content.gallery[$lang]}
			<br />
			{content.cont[$lang]}
			<br />
			{content.art[$lang]}
		</h4>
	</div>
	<div class="subsection">
		<img class="bg-img" src="/blueprint-building.png" alt="kerka building blueprint" />
	</div>
</section>
<section class="main-section">
	<div class="subsection p-20 items-center flex">
		<h1>Kerka</h1>
	</div>
	<div class="subsection p-20 flex items-center align-middle">
		<p>
			{content.opened[$lang]}
			<br /><br />
			{content.andnow[$lang]}
		</p>
	</div>
</section>

<style>
	.main-section {
		border-bottom: 3px solid black;
		height: calc(50vh - 80px);
		display: flex;
		flex-direction: row;
	}
	.subsection {
		width: 50%;
	}
	.subsection:not(:last-child) {
		border-right: 3px dashed black;
	}

	.bg-img {
		width: 100%;
		height: 100%;
		object-fit: cover;
	}
</style>
