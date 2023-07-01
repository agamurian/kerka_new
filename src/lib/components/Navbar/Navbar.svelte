<script lang="ts">
	import { page } from '$app/stores';
	import { backgroundColor, lang, hideNav } from '$lib/stores';
	import { menu } from '$lib/content/common';
	import LangSwitcher from './LangSwitcher.svelte';
	import KerkaNav from '../Icons/KerkaNav.svelte';
	import VerticalNav from './VerticalNav.svelte';
	let lastScrollTop = 0;
</script>

<svelte:window
	on:scroll={() => {
		let scrollTop = window.pageYOffset || document.documentElement.scrollTop;
		if (scrollTop > lastScrollTop) {
			hideNav.set(true);
		} else hideNav.set(false);
		lastScrollTop = scrollTop;
	}}
/>

<nav
	class="sticky top-0 p-0 navbar flex"
	class:hide-nav={$hideNav}
	style="background-color: {$backgroundColor}; height:60px"
>
	<section class="text-left w-15 p-0">
		<a class="m-0 p-0" href="/#">
			<KerkaNav />
		</a>
	</section>

	<div class="flex flex-grow">
		<section style="flex: 1" />
		<section class="w-15 nav-item">
			<LangSwitcher />
		</section>
	</div>
</nav>
<VerticalNav />

<style>
	.nav-item {
		display: flex;
		flex: 0;
		padding: 10px;
		height: 100%;
	}
	.navbar {
		z-index: 2000;
		color: #000;
		font-size: 20px;
		top: 0;
		transition: 0.4s ease-out;
		border-bottom: 3px solid black;
		border-top: 12px solid black;
	}
	.hide-nav {
		top: -60px;
		transition: 0.4s ease-out;
	}
	.active-route {
		text-decoration: underline 4px #000;
	}
</style>
