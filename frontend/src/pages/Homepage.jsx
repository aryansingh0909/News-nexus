import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const HomePage = () => {
    const [news, setNews] = useState([]);
    const navigate = useNavigate();
    function getmain(data)
    {
        const headlineObj =  JSON.parse(data["headline"]);
        const mainHeadline = headlineObj.main;
        return mainHeadline
    }

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await axios.get('http://127.0.0.1:5000/getdata');
                setNews(response.data);
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        };
        fetchData();
    }, []);

    return (
        <div className="min-h-screen bg-gray-100 w-screen">
            <nav className="bg-white shadow-md sticky top-0 z-10 w-screen p-4">
                <div className="container mx-auto flex justify-between items-center">
                    <h1 className="text-4xl font-bold text-indigo-600">News Nexus</h1>
                    <button className="bg-indigo-600 text-white py-2 px-4 rounded-md">Logout</button>
                </div>
            </nav>
            <div className="mt-4 container mx-auto align-middle justify-center" >
                    <input
                        type="text"
                        placeholder="Search..."
                        className="py-2 px-4 w-full md:w-1/2 border align-middle1 border-indigo-300 rounded-md focus:outline-none focus:border-indigo-500"
                    />
                    <button className="bg-indigo m-3 border-black-200" onClick={()=>{navigate('/search');}}>Search</button>
                </div>
            <main className="container mx-auto py-8 my-30">
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 my-30">
                    {news.map((item, index) => (
                        <div key={index} className="bg-white border border-gray-200 rounded-lg shadow dark:bg-gray-800 dark:border-gray-700">
                            <a href="#">
                                <h5 className="p-4 text-xl font-bold text-gray-900 dark:text-white">{`News ${index+1}`}</h5>
                            </a>
                            <p className="p-4 text-gray-700 dark:text-gray-400">{item["abstract"].substring(0, 100)}</p>
                            <a href="#" className="inline-block py-2 px-4 text-sm font-medium text-white bg-blue-700 rounded-lg hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
                                Read more
                            </a>
                        </div>
                    ))}
                </div>
            </main>
        </div>
    );
};

export default HomePage;
