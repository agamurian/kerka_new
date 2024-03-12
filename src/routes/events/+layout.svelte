<div class="content">
	<slot />
</div>

<style>
	.content {
		padding-left: 60px;
  }
  :global(img){
    padding: 0rem;
    max-width: calc(100vw - 4rem - 120px);
    max-height: 90vh;
  }
  :global(p){
    max-width: calc(100vw - 120px - 4rem);
    display: inline-block;
    padding: 3vw;
    line-height: 1.5;
    color: #111;
  }
  :global(hr){
    outline: none;
      border: none;
  border-top: 3px double #333;
  color: #333;
  overflow: visible;
  text-align: center;
  height: 5px;
  }
</style>
