<script>
	import '../app.postcss';
	import Navbar from '$lib/components/Navbar/Navbar.svelte';
	import { page } from '$app/stores';
	$: title = $page.url.pathname.split('/').join(' - ') + ' - Kerka Gallery';
	const description = 'Independent contemprorary art gallery';
</script>

<svelte:head>
	<!--<link rel="stylesheet" href="/tutorial/dark-theme.css">-->
	<title>{title}</title>
	<meta property="og:title" content={title} />
	<meta name="description" content={description} />
	<meta name="twitter:description" content={description} />
	<meta property="og:description" content={description} />

	<meta property="og:image" content="" />
	<meta property="og:image:width" content="200" />
	<meta property="og:image:height" content="200" />
	<meta name="twitter:image" content="" />
	<meta itemprop="image" content="" />
</svelte:head>

<Navbar />
<slot />
