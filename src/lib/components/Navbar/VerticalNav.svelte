<script lang="ts">
	import { page } from '$app/stores';
	import { lang } from '$lib/stores';
	import { menu } from '$lib/content/common';
	import { fade } from 'svelte/transition';
</script>

<div class="nav">
	{#each menu as item}
		<div class="nav-item">
			<a class="mx-5" class:active-route={item.href == $page.route.id} href={item.href}>
				{item[$lang]}
			</a>
		</div>
	{/each}
</div>

<style>
	.nav {
		height: 100vh;
		width: 60px;
		position: fixed;
		left: 0;
		top: 0;
		padding-top: 60px;
		z-index: 2;
		border-right: 3px dashed black;
		text-overflow: ellipsis;
	}
	.nav-item {
		white-space: nowrap;
		writing-mode: vertical-rl;
		transform: rotate(180deg);
		text-orientation: mixed;
		border-top: 3px dashed black;
		text-align: center;
		display: block;
		padding: 15px;
		width: 100%;
		height: calc(25vh - 40px);
	}
</style>
