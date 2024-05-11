<script lang="ts">
	import { page } from '$app/stores';
	import { backgroundColor, lang, hideNav,localtitle } from '$lib/stores';
	import { menu } from '$lib/content/common';
	import LangSwitcher from './LangSwitcher.svelte';
	import KerkaNav from '../Icons/KerkaNav.svelte';
	import VerticalNav from './VerticalNav.svelte';
  let lastScrollTop = 0;
	$: title = $page.url.pathname.split('/').join('/');
  let basecolor = "#000"
  let black = basecolor + "f"
  $: color = basecolor + "0"
  let percentage = "9"
  let hidebale = false
</script>

<svelte:window
	on:scroll={() => {
		let scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    if (window.pageYOffset > 1200){
      hidebale = true
    }
    if (hidebale) {
    if ((scrollTop > lastScrollTop)) {
			hideNav.set(true);
		} else hideNav.set(false);
    } else hideNav.set(false);
    lastScrollTop = scrollTop;
    percentage = window.pageYOffset < 500 ? "0" : "f"
    color = basecolor + percentage
	}}
/>

<nav
	class:hide-nav={$hideNav}
	class="sticky top-0 p-0 navbar flex"
	style="background-color: {$backgroundColor}; height:60px"
>
	<section class="text-left w-15 p-0">
		<a class="m-0 p-0" href="/#">
			<KerkaNav />
		</a>
	</section>

	<div class="flex flex-grow">
		<section style="flex: 1" />
		<section class="w-25 nav-item" style="width: 80vw">
      <div class='bread' style="background-color: #5550; width: 100vw; margin-top: -0.05rem; border:dotted 0.2rem #0000 ">
        <span class='title' style='color: {black};padding-right: 15px;padding-left:15px;border-radius: 0.4rem;'>{title}</span>
        <span class='title' style='color: {color};padding-right: 15px;padding-left:15px;border-radius: 0.4rem;overflow:hidden'>{$localtitle}</span>
      </div>
		</section>
	</div>
	<div class="flex flex-grow">
		<section style="flex: 1" />
		<section class="w-15 nav-item">
			<LangSwitcher />
		</section>
	</div>
</nav>
<VerticalNav />

<style>
  .title{
  transition: 1s ease;
  font-size: 1.0rem;
  font-weight: 600;
  padding: 0.5rem;
  background-color: #0440;
  }
  .title:hover{
  background-color: #0444;
  }
	.nav-item {
		border-left: 3px dashed black;
		display: flex;
		flex: 0;
		padding: 7px 7px 7px 15px;
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
