package com.atooma.plugin.greethumb;

import android.content.Context;

import com.atooma.plugin.Module;

public class GREETHUMB extends Module {

	public static final String MODULE_ID = "GREETHUMB";
	public static final int MODULE_VERSION = 1;

	public GREETHUMB(Context context, String id, int version) {
		super(context, id, version);
	}

	@Override
	public void registerComponents() {
		registerTrigger(new TR_TempExternal(getContext(), "TEMP-EXTERNAL", 1));
		registerTrigger(new TR_TempInternal(getContext(), "TEMP-INTERNAL", 1));
		registerTrigger(new TR_HumExternal(getContext(), "HUM-EXTERNAL", 1));
		registerTrigger(new TR_HumInternal(getContext(), "HUM-INTERNAL", 1));
	}

	@Override
	public void defineUI() {
		setIcon(R.drawable.icon_mod);
		setTitle(R.string.module_name);
	}

	@Override
	public void defineAuth() {
		//Get the username autenticated from activity and define it with setAuthenticated(true, authText);
	}

	@Override
	public void clearCredentials() {
		//Clear
	}

}