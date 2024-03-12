<div class="content">
	<slot />
</div>

<style>
	.content {
		padding-left: 60px;
  }
  :global(img){
    padding: 1rem;
    max-width: 100vw;
    max-height: 90vh;
  }
  :global(p){
    display: inline-block;
    padding: 2rem;
    line-height: 1.5;
    color: #111;
  }
</style>
