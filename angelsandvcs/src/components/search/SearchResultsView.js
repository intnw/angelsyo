import { useState, useEffect } from "react";
import { useSearch } from "../../api/search/useSearch";

import SearchResultInfoView  from "./SearchResultInfoView";
import LoadingView from "../utils/LoadingView";

export default function SearchResultsView({ searchQuery }) {
    const { getSearchResultsByKeywords } = useSearch();
    const [pageNum, setPageNum] = useState(1);
    const [pageOffset, setPageOffset] = useState(1);
    const [totalPages, setTotalPages] = useState(0);
    const [searchResults, setSearchResults] = useState([]);
    const [showSearchResults, setShowSearchResults] = useState(false);
    const [isLoading, setIsloading] = useState(false);

    useEffect(() => {
        search(searchQuery, 1);
    }, [searchQuery])

    useEffect(() => {
        search(searchQuery, pageNum);
    }, [pageNum])

    function search(query, pageNum) {
        if(!query) return;

        setSearchResults([]);
        setIsloading(true);

        getSearchResultsByKeywords({"keywords": query, "pagenum": pageNum})
        .then(jsonResponse => {
           if(jsonResponse.ok) {
                setIsloading(false);
                setShowSearchResults(true);
                setSearchResults(jsonResponse.data);
                const totalPages = Math.floor(jsonResponse.data.total/10);
                setTotalPages(totalPages);
            }
            else {
                setSearchResults([]);
                setIsloading(false);
            }
        })
    }

    function selectSearchResultsPage(selectedPageNum) {
        if(selectedPageNum == pageNum) {
            return "p-1 px-2 md:p-3 md:px-5 text-white bg-slate-700 hover:bg-slate-200 rounded-full cursor-pointer";
        }
        else {
            return "p-1 px-2 md:p-3 md:px-5 hover:bg-slate-200 rounded-full cursor-pointer";
        }
    }

    function currentPage(currPage) {
        // setPageOffset((pageOffset-9)<1? 1: (pageOffset-9));
        setPageNum(currPage);
    }

    function previousPage() {
        setPageOffset((pageOffset-9)<1? 1: (pageOffset-9));
        setPageNum((pageOffset-9)<1? 1: (pageOffset-9));
    }

    function nextPage() {
        setPageOffset((pageOffset+9)>totalPages? totalPages: (pageOffset+9));
        setPageNum((pageOffset+9)>totalPages? totalPages: (pageOffset+9));
    }

    return (
        <div className="flex flex-col w-full justify-center items-center">
            <div className="flex gap-3 w-full md:max-w-5xl h-fit justify-center mt-7 p-3">
                {
                    !isLoading
                    ?
                
                        showSearchResults && searchResults.data.length!==0 &&
                        <div className="flex flex-col w-full">
                            <div className="flex flex-col w-full ">
                                <div className="flex justify-center">
                                    <p className="w-fit font-semibold text-slate-700">Found {searchResults.total} angels for your query! </p>
                                </div>
                                <ul>
                                    {
                                        searchResults.data.map((angelInfo, index) => {
                                            return <SearchResultInfoView key={index} angelInfo={angelInfo} />
                                        })
                                    }
                                </ul>
                            </div>
                            <div className="flex flex-col justify-center items-center mb-20">
                                <div className="w-fit text-xl md:text-3xl text-slate-500">
                                    Yooooooooooooooooooo...
                                </div>
                                <div className="flex w-fit gap-1 text-orange-500 text-md md:text-xl">
                                    {
                                        [...Array(9).keys()].map((num) => {
                                            if((num+pageOffset-1)>totalPages)
                                            return <></> 
                                            else
                                            return <span
                                                className = {selectSearchResultsPage(num+pageOffset)}
                                                onClick={() => currentPage(num+pageOffset)}    
                                            >
                                                {num+pageOffset}
                                            </span>
                                        })
                                    }
                                </div>
                                <div className="flex w-fit gap-1 text-orange-500 text-md md:text-xl">
                                    <span className="p-3 px-5 rounded-full cursor-pointer hover:bg-slate-200"
                                        onClick={() => previousPage()}
                                    >
                                        {'<<'}
                                    </span>
                                    <span className="p-3 px-5 rounded-full cursor-pointer hover:bg-slate-200"
                                        onClick={() => nextPage()}
                                    >
                                        {'>>'}
                                    </span>
                                </div>
                            </div>
                        </div> 
                    :
                    <LoadingView />
                }         
            </div>
        </div>     
    );
}