// elements
const crossSelect = document.getElementById('cross-select')
const realSelect = document.getElementById('3d-real-select')
const complexSelect = document.getElementById('3d-complex-select')
const graphEl = document.getElementById('image')
const selectTable = document.getElementById('select-table')

// get info from url
const urlInfo = window.location.search

// settings
let n = 1 
let l = 0
let m = 0
let mode = 'cross'

// ? on end of url in form of ?mode_n_l_m
if (urlInfo && urlInfo.length > 1) {
  const params = urlInfo.substring(1).split('_')
  let nTemp = parseInt(params[1])
  let lTemp = parseInt(params[2])
  let mTemp = parseInt(params[3])
  let modeTemp = params[0]
  
  if (
    (0 < nTemp && nTemp < 8)
    && (0 <= lTemp && lTemp < nTemp)
    && (-lTemp - 1 < mTemp && mTemp < lTemp + 1 )
    && (mode === 'cross' || mode === '3d-real' || mode === '3d-complex')
  ) {
    mode = modeTemp
    n = nTemp
    l = lTemp
    m = mTemp
  }
}

// set image
const path = `img/${mode}/${n}_${l}_${m}.png`
graphEl.src = path

// mark selected mode
document.getElementById(`${mode}-select`).id = 'selected-mode'

// set up links for mode selection
crossSelect.href = `./?cross_${n}_${l}_${m}`
realSelect.href = `./?3d-real_${n}_${l}_${m}`
complexSelect.href = `./?3d-complex_${n}_${l}_${m}`

// subshell numbers to letters table
subshellTable = {
  0: 's',
  1: 'p',
  2: 'd',
  3: 'f',
  4: 'g',
  5: 'h',
  6: 'i'
}

// create table for orbital selection
for (let nTable = 1; nTable < 8; nTable += 1) {
  let tableRow = `<div style="background-color:hsl(${nTable * 50}, 100%, 80%)">`

  for (let lTable = 0; lTable < nTable; lTable += 1) {
    let subshellSection = `<div class="subshell-container"><div class="links-container">`

    for (let mTable = -lTable; mTable <= lTable; mTable += 1) {
      subshellSection += `<a 
        href="./?${mode}_${nTable}_${lTable}_${mTable}" 
        class="orbital" id="${nTable === n && lTable === l && mTable === m ? "selected-orbital" : ""}">${mTable}
      </a>`
    }

    subshellSection += `</div><div class='labels-container'>${nTable}${subshellTable[lTable]}</div></div>`
    tableRow += subshellSection
  }

  tableRow += '</div>'
  selectTable.innerHTML += tableRow
}