import React from "react";
import { useState, useEffect } from "react";

function App() {
    const [jobIdData, setJobIdData] = useState([]);
    const [jobData, setJobData] = useState([]);

    const fetchData = async (url) => {
        try {
            const res = await fetch(url);

            if (!res.ok) {
                console.log("API ERROR", res.status);
            }
            console.log(res)
            return await res.json();
        } catch (e) {
            console.log("API FAILED", e);
        }
    };

    useEffect(() => {
        const loadData = async () => {
            const data = await fetchData("https://hacker-news.firebaseio.com/v0/jobstories.json");
            if (data) {
                setJobIdData(data);
            }
        };
        loadData()
    }, []);

    useEffect(() => {
        const loadjobs = async (jobId) => {
            const data = await fetchData(`https://hacker-news.firebaseio.com/v0/item/${jobId}.json`);
            if (data) {
                setJobData(prev => [...prev, data]);
            }
        }
        jobIdData.forEach(id => loadjobs(id));
    }, [jobIdData])

    const styles = {
        main: {
            padding: "20px",
        },
        title: {
            color: "#5C6AC4",
        },
    };

    return (
        <div style={styles.main}>
            <h1 style={styles.title}>Hello, World! here</h1>
            <div>
                {jobIdData.map((id) => (
                    <>
                        <div key={id}> <span>Job Id:</span> {id}</div>
                    </>
                ))}
            </div>
            <div>
                {
                    jobData.map((job) => (
                        <div key={job.id}>
                            <h3>{job.title}</h3>
                            <p>{job.url}</p>
                        </div>
                    ))
                }
            </div>


        </div>
    );
}

export default App;
