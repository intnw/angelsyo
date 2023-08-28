import SearchView from "./components/search/SearchView";

//main outer div width and size
//then inner and inner and innermost...
function App() {
  return (
    <div className="flex justify-center p-3 w-screen h-screen min-h-screen overflow-y-auto">
      <SearchView />
    </div>
  );
}

export default App;
