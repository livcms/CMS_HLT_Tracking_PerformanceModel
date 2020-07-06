{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 225
    },
    "colab_type": "code",
    "id": "KcMCAnM6ODBb",
    "outputId": "51bb6a17-c1a7-4537-8d3e-70d4b71dff7a"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting uproot\n",
      "\u001b[?25l  Downloading https://files.pythonhosted.org/packages/0a/52/0e5e295affc168430591b8a687f7ba6c2bb911c766605466e224e2b22069/uproot-3.11.7-py2.py3-none-any.whl (116kB)\n",
      "\u001b[K     |████████████████████████████████| 122kB 2.7MB/s \n",
      "\u001b[?25hCollecting awkward<1.0,>=0.12.0\n",
      "\u001b[?25l  Downloading https://files.pythonhosted.org/packages/99/2f/00ba25d499c969d95dfce221d1ce3556a4400919f803d286c7c6817a108d/awkward-0.12.21-py2.py3-none-any.whl (87kB)\n",
      "\u001b[K     |████████████████████████████████| 92kB 5.4MB/s \n",
      "\u001b[?25hCollecting uproot-methods>=0.7.0\n",
      "  Downloading https://files.pythonhosted.org/packages/d3/68/d848b0ff4d1a30500b26dd570068edf5b30bafbc40500b887ef34d13377b/uproot_methods-0.7.4-py2.py3-none-any.whl\n",
      "Requirement already satisfied: numpy>=1.13.1 in /usr/local/lib/python3.6/dist-packages (from uproot) (1.18.5)\n",
      "Requirement already satisfied: cachetools in /usr/local/lib/python3.6/dist-packages (from uproot) (4.1.0)\n",
      "Installing collected packages: awkward, uproot-methods, uproot\n",
      "Successfully installed awkward-0.12.21 uproot-3.11.7 uproot-methods-0.7.4\n"
     ]
    }
   ],
   "source": [
    "pip install uproot\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "O0CfySO3Ns_c"
   },
   "outputs": [],
   "source": [
    "import uproot\n",
    "import numpy as np\n",
    "import pandas as pd \n",
    "import matplotlib.pyplot as plt \n",
    "import re\n",
    "\n",
    "#DQMFilename = raw_input(\"Please enter filename (must have PU followed by pileup number:\")\n",
    "DQMFilename = \"DQM_noPU_numEvent100.root\" \n",
    "file = uproot.open(DQMFilename)[\"DQMData;1\"][\"Run 1;1\"][\"DQM;1\"][\"Run summary;1\"][\"TimerService;1\"]\n",
    "numevent= re.compile(\"numEvent([0-9]*)\")\n",
    "numevents = int(numevent.findall(DQMFilename)[0])\n",
    "#there are two directories in the Timerservice. Find the names in the first directory\n",
    "plotnames = file.keys()\n",
    "#we are only interested in the time plots, and not by the ones by ls\n",
    "time_plotnames = [name.decode(\"utf-8\") for name in plotnames if (\"time_real\" in name.decode(\"utf-8\"))  & (\"byls\" not in name.decode(\"utf-8\"))]\n",
    "\n",
    "\n",
    "#find names in the second directory, which contains by module info    \n",
    "timebymodule = file[\"process RECO modules;1\"]\n",
    "plotnames_bymodule = timebymodule.keys()\n",
    "time_plotnames_bymodule = [name.decode(\"utf-8\") for name in plotnames_bymodule if (\"time_real\" in name.decode(\"utf-8\")) & (\"byls\" not in name.decode(\"utf-8\"))]\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "k8KocvvPRbNu"
   },
   "outputs": [],
   "source": [
    "#the data is in histograms, so binned. Function to find midpoint of bin. If the upper limit is infinite, set midpoint as the left edge of the bin\n",
    "def midpoint(bins): \n",
    "    if np.isinf(bins.right): \n",
    "        x = bins.left\n",
    "    else: \n",
    "        x = bins.mid\n",
    "    return x\n",
    "\n",
    "\n",
    "\n",
    "times =[]\n",
    "stds =[]\n",
    "#come back and generalise\n",
    "\n",
    "\n",
    "#iterate through each plot and append the average time and standard deviation to lists \n",
    "def read_hists_from_folder(directory, plotnamelist):\n",
    "    for name in plotnamelist: \n",
    "    \n",
    "            timehist = directory[name]\n",
    "            timehistpd = timehist.pandas()\n",
    "             \n",
    "            \n",
    "            #uproot reads all the zeros from the histogram. Read only non_zero values. Bins are an index, reset so they become a column\n",
    "            nonzero_timehist = timehistpd[timehistpd[\"count\"]>0].reset_index()      \n",
    "            nonzero_timehist[\"bin_centres\"] = nonzero_timehist.iloc[:,0].apply(lambda x:  midpoint(x))\n",
    "            if name==\"event time_real;1\": \n",
    "                print(nonzero_timehist[\"bin_centres\"])\n",
    "            #count times bin centre\n",
    "            count_times =nonzero_timehist[\"count\"]*nonzero_timehist[\"bin_centres\"]\n",
    "            avtime =sum(count_times)/numevents\n",
    "            times.append(round(avtime,2))\n",
    "            stds.append(round(np.std(count_times),2))\n",
    "            #numevents = sum(nonzero_timehist[\"count\"])  \n",
    "\n",
    "          "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 225
    },
    "colab_type": "code",
    "id": "N_zvPYgAcH8Q",
    "outputId": "e2d1ba95-4b67-4180-e7eb-9abb69949932"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0       220.25\n",
      "1       231.25\n",
      "2       236.75\n",
      "3       253.25\n",
      "4       259.75\n",
      "        ...   \n",
      "94      927.75\n",
      "95      985.25\n",
      "96     1112.25\n",
      "97     1162.25\n",
      "98    10000.00\n",
      "Name: bin_centres, Length: 99, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "read_hists_from_folder(file, time_plotnames)\n",
    "\n",
    "read_hists_from_folder(timebymodule, time_plotnames_bymodule)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 34
    },
    "colab_type": "code",
    "id": "iDe7jl4ON5nD",
    "outputId": "7de07cf0-912d-4265-988f-86cdfa1a6487"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "747.2999999999997\n"
     ]
    }
   ],
   "source": [
    "\n",
    "\n",
    "res = pd.DataFrame({\n",
    "    #print module names so the string stops where \"time\" begins\n",
    "    \"Module\":  [name[:name.rfind(\"time\")] for name in time_plotnames+time_plotnames_bymodule],\n",
    "    \"Average time/event (ms) at \" + str(int(numevents)) +\" events\": times\n",
    "      #\"Std (ms) at \" +str(int(numevents)) + \" events\" : stds\n",
    "})\n",
    "#pd.set_option(\"display.max_rows\", None, \"display.max_columns\", None)\n",
    "cols = list(res)\n",
    "#since the average time column name is so long, it is displayed first, reshuffle so module comes first \n",
    "cols.insert(0, cols.pop(cols.index(\"Module\")))\n",
    "reordered_res = (res[cols])\n",
    "print(sum(reordered_res.iloc[5:, 1]))\n",
    "reordered_res.to_csv(\"DQM_noPU_numEvent100.csv\")\n",
    "                                               "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 17
    },
    "colab_type": "code",
    "id": "o-rkebrslor_",
    "outputId": "e53e8c87-c68a-4e45-85a8-27d9d64fa72c"
   },
   "outputs": [
    {
     "data": {
      "application/javascript": [
       "\n",
       "    async function download(id, filename, size) {\n",
       "      if (!google.colab.kernel.accessAllowed) {\n",
       "        return;\n",
       "      }\n",
       "      const div = document.createElement('div');\n",
       "      const label = document.createElement('label');\n",
       "      label.textContent = `Downloading \"${filename}\": `;\n",
       "      div.appendChild(label);\n",
       "      const progress = document.createElement('progress');\n",
       "      progress.max = size;\n",
       "      div.appendChild(progress);\n",
       "      document.body.appendChild(div);\n",
       "\n",
       "      const buffers = [];\n",
       "      let downloaded = 0;\n",
       "\n",
       "      const channel = await google.colab.kernel.comms.open(id);\n",
       "      // Send a message to notify the kernel that we're ready.\n",
       "      channel.send({})\n",
       "\n",
       "      for await (const message of channel.messages) {\n",
       "        // Send a message to notify the kernel that we're ready.\n",
       "        channel.send({})\n",
       "        if (message.buffers) {\n",
       "          for (const buffer of message.buffers) {\n",
       "            buffers.push(buffer);\n",
       "            downloaded += buffer.byteLength;\n",
       "            progress.value = downloaded;\n",
       "          }\n",
       "        }\n",
       "      }\n",
       "      const blob = new Blob(buffers, {type: 'application/binary'});\n",
       "      const a = document.createElement('a');\n",
       "      a.href = window.URL.createObjectURL(blob);\n",
       "      a.download = filename;\n",
       "      div.appendChild(a);\n",
       "      a.click();\n",
       "      div.remove();\n",
       "    }\n",
       "  "
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {
      "tags": []
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "application/javascript": [
       "download(\"download_f696f3a4-ecad-4eb6-a03c-bee12faaad91\", \"DQM_noPU_numEvent100.csv\", 5238)"
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {
      "tags": []
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "from google.colab import files\n",
    "files.download('DQM_noPU_numEvent100.csv') "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "EmUnGi3ISMOY"
   },
   "outputs": [],
   "source": [
    "timehist = file['event time_real;1']\n",
    "timehistpd = timehist.pandas()\n",
    "             \n",
    "            \n",
    "            # #uproot reads all the zeros from the histogram. Read only non_zero values. Bins are an index, reset so they become a column\n",
    "            # nonzero_timehist = timehistpd[timehistpd[\"count\"]>0].reset_index()      \n",
    "            # nonzero_timehist[\"bin_centres\"] = nonzero_timehist.iloc[:,0].apply(lambda x:  midpoint(x))\n",
    "            # if name==\"event time_real;1\": \n",
    "            #     print(nonzero_timehist[\"bin_centres\"])\n",
    "            # #count times bin centre\n",
    "            # count_times =nonzero_timehist[\"count\"]*nonzero_timehist[\"bin_centres\"]\n",
    "            # avtime =sum(count_times)/numevents\n",
    "            # times.append(round(avtime,2))\n",
    "            # stds.append(round(np.std(count_times),2))\n",
    "            # #numevents = sum(nonzero_timehist[\"count\"])  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 104
    },
    "colab_type": "code",
    "id": "tN03Bl2qTY0z",
    "outputId": "0becc53d-94d4-47a6-cca0-7226238a027e"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[\"b'event time_real;1'\",\n",
       " \"b'explicit time_real;1'\",\n",
       " \"b'overhead time_real;1'\",\n",
       " \"b'process RECO time_real;1'\",\n",
       " \"b'source time_real;1'\"]"
      ]
     },
     "execution_count": 28,
     "metadata": {
      "tags": []
     },
     "output_type": "execute_result"
    }
   ],
   "source": [
    "time_plotnames"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "rZpPIkZqTbXw"
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "colab": {
   "name": "Untitled20.ipynb",
   "provenance": [],
   "toc_visible": true
  },
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}
