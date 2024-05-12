<script lang="ts">
	import { page } from '$app/stores';
	import { lang,theme,white,black } from '$lib/stores';
	import { menu } from '$lib/content/common';
</script>

<div class="nav"
     style="
     border-right: 3px solid {($theme == 'dark')  ? $white : $black};"
  >
	{#each menu as item}
		<a href={item.href}>
      <div class="nav-item"
     style="
     border-top: 3px dashed {($theme == 'dark')  ? $white : $black};"
        class:active={item.href == $page.route.id}>
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
		text-overflow: ellipsis;
	}
	.nav-item {
		white-space: nowrap;
		writing-mode: vertical-rl;
		transform: rotate(180deg);
		text-orientation: mixed;
		text-align: center;
		display: block;
		padding: 15px;
		width: 100%;
		height: calc(25vh - 40px);
	}

	.nav-item:hover {
		background-color: #888;
	}

	.active {
		background-color: #888;
	}
</style>
