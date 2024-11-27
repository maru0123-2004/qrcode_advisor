<script>
  import Button from "flowbite-svelte/Button.svelte";
  import Card from "flowbite-svelte/Card.svelte";
  import Modal from "flowbite-svelte/Modal.svelte";
  import ArrowRightOutline from 'flowbite-svelte-icons/ArrowRightOutline.svelte';

  let isModalOpen = false;

  // モーダルを開く
  function openModal() {
    isModalOpen = true;
  }

  // モーダルを閉じる
  function closeModal() {
    isModalOpen = false;
  }

  // バス停情報
  const busStops = [
    { id: 1, name: "中央駅", time: "09:00" },
    { id: 2, name: "公園前", time: "09:15" },
    { id: 3, name: "図書館入口", time: "09:30" },
    { id: 4, name: "市役所前", time: "09:45" },
    { id: 5, name: "終点: 駅南口", time: "10:00" }
  ];
</script>

<style>
  /* 全体を中央揃えにするスタイル */
  .center-container {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    background-color: #f9fafb;
  }

  .card-container {
    max-width: 400px;
    text-align: center;
  }

  /* バス停カードのリスト */
  .bus-stop-list {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 1rem; /* カード間のスペース */
  }
</style>

<div class="center-container">
  <div class="card-container">
    <Card>
      <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">
        このバスは目的地へ行きます
      </h5>
      <p class="mb-3 font-normal text-gray-700 dark:text-gray-400 leading-tight">
        途中バス停を見る場合はボタンをクリックしてください。
      </p>
      <Button class="w-fit mx-auto" on:click={openModal}>
        途中バス停を見る
        <ArrowRightOutline class="w-6 h-6 ms-2 text-white" />
      </Button>
    </Card>
  </div>
</div>

<!-- モーダル -->
<Modal bind:open={isModalOpen}>
  <h2 class="text-xl font-bold mb-4">途中バス停一覧</h2>

  <!-- バス停カードをリストとして表示 -->
  <div class="bus-stop-list">
    {#each busStops as stop (stop.id)}
      <Card>
        <h5 class="text-lg font-bold">{stop.name}</h5>
        <p class="text-gray-700">到着予定時刻: {stop.time}</p>
      </Card>
    {/each}
  </div>

  <Button color="red" on:click={closeModal} class="mt-4">
    閉じる
  </Button>
</Modal>
