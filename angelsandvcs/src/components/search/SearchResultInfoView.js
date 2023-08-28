
import TwitterLogo from "../../images/twitter.svg";
import LinkedinLogo from "../../images/linkedin.svg";
import EmailLogo from "../../images/email.svg";

export default function SearchResultInfoView({ angelInfo }) {

    function prettyInfo(info) {
        if(info.value) {
            return info.value
        }
        else {
            return "---"
        }
    }

    function prettyEmail(info) {
        // if(info)
        // return <a className="inline-block p-1" href={`mailto:${info}`} target="_blank" rel="noopener noreferrer">
        //     <img className="w-7 h-7" src={EmailLogo} alt={info} />
        // </a>
        // else 
        return <></>;
    }

    function prettyTwitter(info) {
        if(info)
        return <a className="inline-block p-1" href={`https://twitter.com/${info}`} target="_blank" rel="noopener noreferrer">
            <img className="w-7 h-7" src={TwitterLogo} alt={info} />
        </a>
        else return <></>;
    }

    function prettyLinkedin(info) {
        if(info)
        return <a className="inline-block p-1" href={info} target="_blank" rel="noopener noreferrer">
            <img className="w-7 h-7" src={LinkedinLogo} alt={info} />
        </a>
        else return <></>;
    }
    
    return (
        <li className="flex w-full my-3 p-3 border border-slate-300 rounded-xl">
            {
                <div className="w-full">
                    <span className="text-xl font-semibold">
                        {`${angelInfo[0].value} ${angelInfo[1].value}`}
                    </span>
                    <br />
                    <div className="w-full p-3">
                        { prettyInfo(angelInfo[3]) }
                    </div>    
                    <span>
                        {`${angelInfo[6].value} ${angelInfo[7].value} ${angelInfo[8].value}`}
                    </span>
                    <div className="flex justify-between p-3">
                        <div className="flex items-center font-mono">
                            {`${angelInfo[4].value} ${angelInfo[5].value}`}
                        </div>
                        <div className="flex justify-end items-center content-end">
                            { prettyEmail(angelInfo[9].value) } {  prettyLinkedin(angelInfo[10].value) } {  prettyTwitter(angelInfo[11].value) }
                        </div>
                    </div>
                    
                </div>
            }
        </li>
    );
}