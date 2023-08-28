import { useState, useEffect } from "react";

import LoadingSpinner from "../../images/loading-icon.gif";
import Rhombus from "../../images/Rhombus.gif";
import Loading1484 from "../../images/1484.gif";
import Loading1485 from "../../images/1485.gif";
import LoadingWalk from "../../images/Walk.gif";
import LoadingSpinner1 from "../../images/Iphone-spinner-2.gif";

export default function LoadingView() {
    const [isLoading, setIsloading] = useState(false);
    
    return (
        <div className="flex w-full justify-center items-center">
            <img className="w-18 h-18" src={LoadingSpinner} alt="loading" />
        </div>
    );
}