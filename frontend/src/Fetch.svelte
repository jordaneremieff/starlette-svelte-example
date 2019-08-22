<script>
    import { onMount } from "svelte";
    let data = [];
    onMount(async function() {
        const response = await fetch("http://localhost:8000/high-scores/");
        const json = await response.json();
        data = json;
    });

    async function handleInsert() {
        const form = document.getElementById('insertForm');
        const formData = new FormData();
        formData.append('name', form.name.value);
        formData.append('score', form.score.value);
        const response = await fetch("http://localhost:8000/high-scores/", {
            method: 'post',
            body: formData,
        })
        const json = await response.json();
        let table = document.getElementById("highScoreTable").getElementsByTagName("tbody")[0];
        let row   = table.insertRow(table.rows.length);
        let rowData = `<td>${json.name}</td><td>${json.score}</td>`;
        row.innerHTML = rowData;
    }
</script>

<style>
    table {
        width: 50%;
    }
</style>

<h1>High Scores</h1>
<table id="highScoreTable">
    <thead align="left">
        <th>Name</th>
        <th>Score</th>
    </thead>
    <tbody>
        {#each data as row}
        <tr><td>{row.name}</td><td>{row.score}</td></tr>
        {/each}
    </tbody>
</table>
<br>
<h3>Add new score</h3>
<form id="insertForm">
Name: <input type="text" name="name" />
Score: <input type="number" name="score" />
</form>
<button on:click={handleInsert}>Insert</button>