<script lang="ts">
	import { page } from '$app/stores';
	import { backgroundColor, lang, hideNav } from '$lib/stores';
	import { menu } from '$lib/content/common';
	import LangSwitcher from './LangSwitcher.svelte';
	import NavbarMenu from './NavbarMenu.svelte';
	import KerkaNav from '../Icons/KerkaNav.svelte';
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
	style="background-color: {$backgroundColor}; height:80px"
>
	<section class="text-left w-15 p-0">
		<a class="m-0 p-0" href="/#">
			<KerkaNav />
		</a>
	</section>

	<div class="hidden md:flex md:flex-grow">
		<section class="text-center flex-grow">
			{#each menu as item}
				<div class="nav-item">
					<a class="mx-5" class:active-route={item.href == $page.route.id} href={item.href}>
						{item[$lang]}
					</a>
				</div>
			{/each}
		</section>
		<section class="w-15 nav-item">
			<LangSwitcher />
		</section>
	</div>

	<div class="flex flex-grow flex-row-reverse md:hidden">
		<NavbarMenu />
	</div>
</nav>

<style>
	.nav-item {
		border-left: 3px dashed black;
		display: inline-block;
		padding: 19px;
		height: 100%;
	}
	.navbar {
		z-index: 2000;
		color: #000;
		font-size: 20px;
		top: 0;
		transition: 0.4s ease-out;
		border-bottom: 3px solid black;
		border-top: 10px solid black;
	}
	.hide-nav {
		top: -80px;
		transition: 0.4s ease-out;
	}
	.active-route {
		text-decoration: underline 4px #000;
	}
</style>
