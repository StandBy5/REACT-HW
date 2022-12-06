package kr.lucypark.jhannanum.comm;

/* Copyright 2014 Lucy Park <me@lucypark.kr> */

import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedList;
import java.util.List;
import java.util.Objects;

import kr.ac.kaist.swrc.jhannanum.comm.Eojeol;
import kr.ac.kaist.swrc.jhannanum.comm.Sentence;
import kr.ac.kaist.swrc.jhannanum.exception.ResultTypeException;
import kr.ac.kaist.swrc.jhannanum.hannanum.Workflow;
import kr.lucypark.jhannanum.hannanum.WorkflowFactory;

public class HannanumInterface {
    private Workflow wfMorph = null;
    private Workflow wfNoun = null;
    private Workflow wfPos09 = null;
    private Workflow wfPos22 = null;

    public String morphAnalyzer(String phrase) {
        if (phrase == null || Objects.equals(phrase, "") || phrase.length() == 0) {
            return null;
        }
        try {
            if (wfMorph == null) {
                wfMorph = WorkflowFactory.getPredefinedWorkflow(WorkflowFactory.WORKFLOW_MORPH_ANALYZER);
                wfMorph.activateWorkflow(false);
            }
            wfMorph.analyze(phrase);
            return wfMorph.getResultOfDocument();
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        } finally {
            closeWorkFlow(wfMorph);
        }
    }

    public String[] extractNoun(String phrase) throws ResultTypeException {
        if (phrase == null || Objects.equals(phrase, "") || phrase.length() == 0) {
            return new String[]{""};
        }
        try {
            if (wfNoun == null) {
                wfNoun = WorkflowFactory.getPredefinedWorkflow(WorkflowFactory.WORKFLOW_NOUN_EXTRACTOR);
                wfNoun.activateWorkflow(false);
            }
            wfNoun.analyze(phrase);
            LinkedList<Sentence> resultList = wfNoun.getResultOfDocument(new Sentence(0, 0, false));
            List<String> list = new ArrayList<>();
            for (Sentence s : resultList) {
                Eojeol[] eojeolArray = s.getEojeols();
                for (Eojeol anEojeolArray : eojeolArray) {
                    if (anEojeolArray.length > 0) {
                        String[] morphemes = anEojeolArray.getMorphemes();
                        Collections.addAll(list, morphemes);
                    }
                }
            }
            return list.toArray(new String[list.size()]);
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        } fina