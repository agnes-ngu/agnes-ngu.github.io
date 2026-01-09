PREVIOUS CODE: ROTATING SMALL CENTERED BUTTON VINYL


#TitleText {
    grid-row: 1;
    position: absolute;
    z-index: 2;
    /*display: flex;
    flex-direction: column;
    justify-content: space-evenly;*/
}

#buttonCombo {
    grid-row: 2;
    position: absolute;
}

#vinylBtn {
    height: 250px;
    width: 250px;
    background: white;
    color: black;
    border: none;
    border-radius: 50%;
    z-index: 2;
    cursor: pointer;

    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    transition: background-color .7s, width .7s ease, height .7s ease;
}

#vinylImg {
    width: 250px;
    height: 250px;
    border-radius: 50%;
    transition: background-color .7s, width .7s ease, height .7s ease;

    animation-name: spin;
    animation-duration: 7s;
    animation-timing-function: linear;
    animation-iteration-count: infinite;
}

#overlayBtn {
    width: 75px;
    height: 75px;
    border-radius: 50%;
    background-color: white;
    border: none;
    cursor: pointer;
    z-index: 3;
    font-family: Arial, Helvetica, sans-serif;
    font-size: 1.5rem;
    font-weight: 800;

    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    transition: background-color .7s, width .7s ease, height .7s ease;
}

#vinylBtn:hover, #vinylImg:hover {
    background: gold;
    height: 270px;
    width: 270px;
    /*animation-duration: 3s;*/
}

#vinylBtn:hover + #overlayBtn, #overlayBtn:hover {
    background-color: gold;
    width: 85px;
    height: 85px;
}

#vinylBtn:has(+ #overlayBtn:hover) {
    background-color: gold;
    height: 270px;
    width: 270px;
    animation-duration: 3s;
}
