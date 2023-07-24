<script lang="ts">
	import { page } from '$app/stores';
	import { lang } from '$lib/stores';
	import { menu } from '$lib/content/common';
</script>

<div class="nav">
	{#each menu as item}
		<a href={item.href}>
			<div class="nav-item" class:active={item.href == $page.route.id}>
				<span class="mx-5">
					{item[$lang]}
				</span>
			</div>
		</a>
	{/each}
</div>

<style>
	span {
		text-rendering: optimizeLegibility;
	}
	a {
		text-decoration: none;
	}
	.nav {
		height: 100vh;
		width: 60px;
		position: fixed;
		left: 0;
		top: 0;
		padding-top: 59.5px;
		z-index: 2;
		border-right: 3px solid black;
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

	.nav-item:hover {
		background-color: #888;
		color: white;
	}

	.active {
		color: white;
		background-color: black;
	}
</style>
